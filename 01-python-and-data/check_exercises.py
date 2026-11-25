"""Tự kiểm tra hành vi bài làm; không sửa file bài tập hay xem đáp án tự động."""

import argparse
from copy import deepcopy
import csv
import importlib.util
import json
import math
from pathlib import Path
import tempfile

STAGE = Path(__file__).resolve().parent
FOLDERS = {
    "01": "01-python-basics",
    "02": "02-functions-and-validation",
    "03": "03-csv-and-json",
    "04": "04-numpy",
    "05": "05-pandas",
    "06": "06-csv-pipeline",
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: cần {expected!r}, nhận {actual!r}")


def raises_value_error(function, argument):
    try:
        function(argument)
    except ValueError:
        return
    raise AssertionError(f"Đầu vào {argument!r} cần báo ValueError")


def load_lesson(number, source):
    path = STAGE / FOLDERS[number] / (source + ".py")
    spec = importlib.util.spec_from_file_location("lesson_" + number + "_" + source, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_01(m):
    for price, percent, expected in [(100000, 20, 80000), (100, 0, 100),
                                     (100, 100, 0), (20.5, 12.5, 17.9375)]:
        actual = m.discounted_price(price, percent)
        require(math.isclose(actual, expected), "Kiểm tra lại công thức giảm giá")
    for score, expected in [(0, "chưa đạt"), (4.9, "chưa đạt"),
                            (5, "đạt"), (10, "đạt")]:
        equal(m.classify_score(score), expected, f"Phân loại điểm {score}")
    equal(m.count_passed([8, 6, 10, 4, 7]), 4, "Đếm người đạt")
    equal(m.count_passed([]), 0, "Danh sách rỗng")
    equal(m.count_passed([5, 0, 5]), 2, "Điểm đúng bằng ngưỡng")


def check_02(m):
    for raw, expected in [("0", 0.), (" 7.5 ", 7.5), (10, 10.)]:
        actual = m.parse_score(raw)
        require(isinstance(actual, float), "parse_score phải trả float")
        equal(actual, expected, "Chuyển điểm hợp lệ")
    for raw in ["", None, "abc", -1, 11, "nan", "inf", "-inf"]:
        raises_value_error(m.parse_score, raw)
    values = ["8", "", "abc", "11", "6"]
    before = values.copy()
    equal(m.separate_scores(values), ([8., 6.], 3), "Tách đúng/sai")
    equal(values, before, "Không sửa danh sách gốc")
    equal(m.separate_scores([]), ([], 0), "Tách danh sách rỗng")


def check_03(m):
    records = m.read_csv(STAGE / "data" / "scores_clean.csv")
    equal(len(records), 5, "Số bản ghi")
    equal(records[0]["score"], "8", "Giữ chuỗi khi đọc CSV")
    before = deepcopy(records)
    report = m.build_report(records)
    equal(report, {"row_count": 5, "mean_score": 7.}, "Báo cáo sạch")
    equal(records, before, "Không sửa bản ghi gốc")
    equal(m.build_report([]), {"row_count": 0, "mean_score": None}, "Tập rỗng")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "new_directory" / "report.json"
        value = dict(report, notes="Tiếng Việt")
        before = deepcopy(value)
        m.write_json(path, value)
        equal(json.loads(path.read_text(encoding="utf-8")), value, "Đọc lại JSON")
        equal(value, before, "Không sửa báo cáo đầu vào")


def check_04(m):
    import numpy as np
    X = np.array([[1., 2.], [3., 4.]])
    before = X.copy()
    mean, std = m.column_statistics(X)
    np.testing.assert_allclose(mean, [2., 3.])
    np.testing.assert_allclose(std, [1., 1.])
    np.testing.assert_allclose(m.standardize(X, mean, std), [[-1., -1.], [1., 1.]])
    np.testing.assert_allclose(m.predict(X, np.array([2., 1.]), 1.), [5., 11.])
    np.testing.assert_allclose(m.standardize(np.array([[5., 6.]]), mean, std), [[3., 3.]])
    constant = np.array([[2., 1.], [2., 3.]])
    c_mean, c_std = m.column_statistics(constant)
    np.testing.assert_allclose(m.standardize(constant, c_mean, c_std), [[0., -1.], [0., 1.]])
    np.testing.assert_array_equal(X, before)
    np.testing.assert_array_equal(mean, [2., 3.])
    np.testing.assert_array_equal(std, [1., 1.])


def check_05(m):
    import pandas as pd
    df = pd.read_csv(STAGE / "data" / "scores_raw.csv", dtype=str, keep_default_na=False)
    before = df.copy(deep=True)
    clean = m.clean_data(df)
    equal(len(clean), 5, "Số dòng sạch")
    equal(clean["id"].tolist(), ["S01", "S02", "S03", "S04", "S08"], "Giữ đúng hàng")
    require(pd.api.types.is_numeric_dtype(clean["score"]), "score phải là kiểu số")
    equal(m.mean_by_group(clean), {"A": 7., "B": 7.}, "Thống kê theo nhóm")
    pd.testing.assert_frame_equal(df, before)
    special = pd.DataFrame({"id": ["X", "X", "Y", "Z"], "name": ["An"] * 4,
                            "group": ["A"] * 4, "score": ["abc", "7", "inf", "nan"]})
    result = m.clean_data(special)
    equal(result["id"].tolist(), ["X"], "Lọc điểm trước khi loại trùng")
    equal(float(result.iloc[0]["score"]), 7., "Giữ lần hợp lệ sau lần sai")
    empty = m.clean_data(df.iloc[:0].copy())
    equal(m.mean_by_group(empty), {}, "Thống kê nhóm rỗng")


def check_06(m):
    records = m.read_csv(STAGE / "data" / "scores_raw.csv")
    before = deepcopy(records)
    valid, rejected = m.clean_data(records)
    equal((len(valid), len(rejected)), (5, 4), "Phân loại bản ghi")
    equal([row["id"] for row in valid], ["S01", "S02", "S03", "S04", "S08"], "Mã được giữ")
    equal([row["record_number"] for row in rejected], [6, 7, 8, 9], "Vị trí lỗi")
    require(all(isinstance(row["reason"], str) and row["reason"].strip()
                for row in rejected), "Mỗi lỗi phải có lý do không rỗng")
    equal([row["data"] for row in rejected], records[4:8], "Giữ dữ liệu lỗi gốc")
    equal(records, before, "Không sửa dữ liệu đầu vào")
    expected = {"valid_count": 5, "mean_score": 7., "passed_count": 4,
                "by_group": {"A": {"count": 2, "mean_score": 7.},
                              "B": {"count": 3, "mean_score": 7.}}}
    summary = m.summarize(valid)
    equal(summary, expected, "Báo cáo dữ liệu sạch")
    empty = {"valid_count": 0, "mean_score": None, "passed_count": 0, "by_group": {}}
    equal(m.summarize([]), empty, "Báo cáo không có dòng hợp lệ")
    special = [{"id": " X ", "name": " An ", "group": " A ", "score": score}
               for score in ["abc", "7", "8", "nan", "inf"]]
    kept, errors = m.clean_data(special)
    equal(kept, [{"id": "X", "name": "An", "group": "A", "score": 7.}], "Chuẩn hóa và chọn mã")
    equal(len(errors), 4, "Điểm không hữu hạn và mã trùng")
    for field in ["id", "name", "group"]:
        row = {"id": "X", "name": "An", "group": "A", "score": "7"}
        row[field] = " "
        equal(len(m.clean_data([row])[1]), 1, "Từ chối trường rỗng " + field)
    with tempfile.TemporaryDirectory() as directory:
        base = Path(directory)
        for index, content in enumerate([
            "id,name,score\nX,An,7\n", "id,name,group,score\nX,An,A,7,extra\n",
            "id,name,group,score\nX,An,A\n", "id,name,id,score\nX,An,X,7\n"]):
            path = base / ("invalid_" + str(index) + ".csv")
            path.write_text(content, encoding="utf-8")
            raises_value_error(m.read_csv, path)
        header_only = base / "empty.csv"
        header_only.write_text("id,name,group,score\n", encoding="utf-8")
        equal(m.read_csv(header_only), [], "CSV chỉ có tiêu đề")
        output = base / "new" / "output"
        m.write_results(output, valid, rejected, summary)
        report = json.loads((output / "summary.json").read_text(encoding="utf-8"))
        equal(report, dict(expected, total_count=9, rejected_count=4), "JSON báo cáo")
        equal(json.loads((output / "rejected.json").read_text(encoding="utf-8")), rejected, "JSON lỗi")
        with (output / "clean.csv").open(encoding="utf-8-sig", newline="") as stream:
            equal([row["id"] for row in csv.DictReader(stream)],
                  [row["id"] for row in valid], "CSV kết quả")
        snapshots = {p.name: p.read_bytes() for p in output.iterdir()}
        m.write_results(output, valid, rejected, summary)
        equal({p.name: p.read_bytes() for p in output.iterdir()}, snapshots, "Chạy lại không đổi kết quả")
        m.write_results(output, [], [], empty)
        equal(json.loads((output / "summary.json").read_text(encoding="utf-8")),
              dict(empty, total_count=0, rejected_count=0), "Ghi báo cáo rỗng")


CHECKS = {"01": check_01, "02": check_02, "03": check_03,
          "04": check_04, "05": check_05, "06": check_06}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--lesson", choices=list(FOLDERS))
    group.add_argument("--all", action="store_true")
    parser.add_argument("--source", choices=["exercises", "solutions"], default="exercises")
    args = parser.parse_args()
    numbers = list(FOLDERS) if args.all else [args.lesson]
    passed = 0
    print("Đang kiểm tra:", "BÀI TỰ LÀM" if args.source == "exercises" else "ĐÁP ÁN THAM KHẢO")
    for number in numbers:
        try:
            CHECKS[number](load_lesson(number, args.source))
        except NotImplementedError as exc:
            print(f"CHƯA XONG bài {number}: {exc}")
        except ModuleNotFoundError as exc:
            print(f"THIẾU THƯ VIỆN bài {number}: {exc.name}; xem bài 00 để cài gói.")
        except Exception as exc:
            print(f"CẦN SỬA bài {number}: {type(exc).__name__}: {exc}")
        else:
            print(f"ĐẠT bài {number}: đã vượt các trường hợp mẫu.")
            passed += 1
    print(f"Kết quả: {passed}/{len(numbers)} bài đạt.")
    if args.source == "solutions":
        print("Đây là kết quả của đáp án, chưa phản ánh bài tự làm của bạn.")
    return 0 if passed == len(numbers) else 1


if __name__ == "__main__":
    raise SystemExit(main())
