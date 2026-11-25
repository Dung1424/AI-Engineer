import pytest
from fastapi.testclient import TestClient

from app.main import create_app

BASE_URL = "/api/v1/products"
PRODUCT = {"name": "Sổ tay", "price_vnd": 35000, "stock": 12, "description": "Giấy kẻ ngang"}


def test_complete_crud_lifecycle(client):
    assert client.get(BASE_URL).json() == {"items": [], "total": 0, "page": 1, "page_size": 5}
    response = client.post(BASE_URL, json=dict(PRODUCT, name="  Sổ tay  "))
    assert response.status_code == 201
    product = response.json()
    assert product["id"] > 0
    assert product["name"] == "Sổ tay"
    assert product["price_vnd"] == 35000
    path = f"{BASE_URL}/{product['id']}"
    assert client.get(path).json() == product
    updated = dict(PRODUCT, name="Sổ tay mới", price_vnd=45000, stock=0)
    response = client.put(path, json=updated)
    assert response.status_code == 200
    assert response.json() == dict(updated, id=product["id"])
    assert client.get(BASE_URL).json()["items"] == [response.json()]
    response = client.delete(path)
    assert response.status_code == 204
    assert response.content == b""
    assert client.get(path).status_code == 404
    assert client.get(BASE_URL).json()["total"] == 0


@pytest.mark.parametrize("changes", [
    {"name": "   "}, {"name": "x" * 121}, {"name": None},
    {"price_vnd": -1}, {"price_vnd": 1.5}, {"price_vnd": "35000"},
    {"price_vnd": True}, {"price_vnd": 1_000_000_000_001},
    {"stock": -1}, {"stock": 1.5}, {"stock": 1_000_001},
    {"description": "x" * 1001}, {"description": None}, {"id": 99},
])
def test_invalid_input_does_not_write_data(client, changes):
    response = client.post(BASE_URL, json=dict(PRODUCT, **changes))
    assert response.status_code == 422
    assert response.json()["detail"] == "Dữ liệu không hợp lệ."
    assert response.json()["errors"][0]["message"]
    assert client.get(BASE_URL).json()["total"] == 0


def test_missing_fields_and_malformed_json(client):
    assert client.post(BASE_URL, json={"name": "Sổ tay"}).status_code == 422
    response = client.post(BASE_URL, content="{invalid", headers={"Content-Type": "application/json"})
    assert response.status_code == 422
    assert client.get(BASE_URL).json()["total"] == 0


def test_missing_products_return_404(client):
    for response in [client.get(BASE_URL + "/999"),
                     client.put(BASE_URL + "/999", json=PRODUCT),
                     client.delete(BASE_URL + "/999")]:
        assert response.status_code == 404
        assert "Không tìm thấy sản phẩm" in response.json()["detail"]


def test_invalid_update_keeps_original_data(client):
    product = client.post(BASE_URL, json=PRODUCT).json()
    path = f"{BASE_URL}/{product['id']}"
    assert client.put(path, json=dict(PRODUCT, price_vnd=-100)).status_code == 422
    assert client.get(path).json() == product


def test_put_replaces_optional_fields_with_defaults(client):
    product = client.post(BASE_URL, json=PRODUCT).json()
    response = client.put(f"{BASE_URL}/{product['id']}", json={"name": "Bút", "price_vnd": 0})
    assert response.status_code == 200
    assert response.json()["description"] == ""
    assert response.json()["stock"] == 0


def test_search_pagination_and_literal_wildcards(client):
    for index in range(7):
        assert client.post(BASE_URL, json=dict(PRODUCT, name=f"Sổ tay {index}")).status_code == 201
    assert client.post(BASE_URL, json=dict(PRODUCT, name="Chất liệu 100% tự nhiên")).status_code == 201
    first = client.get(BASE_URL, params={"q": "Sổ tay", "page": 1, "page_size": 3}).json()
    second = client.get(BASE_URL, params={"q": "Sổ tay", "page": 2, "page_size": 3}).json()
    assert first["total"] == second["total"] == 7
    assert len(first["items"]) == len(second["items"]) == 3
    assert first["items"][0]["name"] == "Sổ tay 6"
    assert not {row["id"] for row in first["items"]} & {row["id"] for row in second["items"]}
    assert client.get(BASE_URL, params={"q": "%"}).json()["total"] == 1
    assert client.get(BASE_URL, params={"q": "' OR 1=1 --"}).json()["total"] == 0
    assert client.get(BASE_URL, params={"page": 100}).json()["items"] == []


@pytest.mark.parametrize("params", [{"page": 0}, {"page_size": 0}, {"page_size": 51}, {"q": "x" * 121}])
def test_pagination_and_search_limits(client, params):
    assert client.get(BASE_URL, params=params).status_code == 422


def test_data_survives_application_restart(settings):
    with TestClient(create_app(settings)) as first_client:
        product = first_client.post(BASE_URL, json=PRODUCT).json()
    with TestClient(create_app(settings)) as second_client:
        assert second_client.get(f"{BASE_URL}/{product['id']}").json() == product


def test_frontend_and_swagger_are_served(client):
    page = client.get("/")
    assert page.status_code == 200
    assert "Quản lý sản phẩm" in page.text
    for path in ["/static/styles.css", "/static/app.js", "/static/api.js", "/docs", "/openapi.json"]:
        assert client.get(path).status_code == 200
