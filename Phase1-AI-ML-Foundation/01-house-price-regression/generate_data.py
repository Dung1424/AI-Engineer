from pathlib import Path

import numpy as np
import pandas as pd


def main() -> None:
    rng = np.random.default_rng(42)
    count = 800
    districts = rng.choice(["center", "east", "west", "south"], count)
    district_bonus = pd.Series(districts).map({"center": 120, "east": 55, "west": 35, "south": 20}).to_numpy()
    area = rng.integers(35, 220, count)
    bedrooms = np.clip((area / 38 + rng.normal(0, 0.7, count)).round(), 1, 6).astype(int)
    age = rng.integers(0, 35, count)
    distance_km = rng.uniform(0.5, 25, count).round(1)
    price = 65 + area * 2.2 + bedrooms * 12 - age * 1.3 - distance_km * 2.1 + district_bonus + rng.normal(0, 24, count)
    data = pd.DataFrame({
        "area_m2": area,
        "bedrooms": bedrooms,
        "age_years": age,
        "distance_km": distance_km,
        "district": districts,
        "price_thousand": price.round(2),
    })
    Path("data").mkdir(exist_ok=True)
    data.to_csv("data/houses.csv", index=False)
    print(f"Đã tạo {len(data)} mẫu tại data/houses.csv")


if __name__ == "__main__":
    main()
