const baseUrl = "/api/v1/products";
const fieldLabels = { name: "Tên sản phẩm", price_vnd: "Giá bán", stock: "Tồn kho", description: "Mô tả" };

async function request(path = "", options = {}) {
  let response;
  try {
    response = await fetch(baseUrl + path, {
      ...options,
      headers: { Accept: "application/json", ...(options.body ? { "Content-Type": "application/json" } : {}) },
    });
  } catch {
    throw new Error("Không kết nối được với API. Kiểm tra ứng dụng Python đang chạy.");
  }
  if (response.status === 204) return null;
  const data = await response.json().catch(() => null);
  if (!response.ok) {
    const firstError = data?.errors?.[0];
    const detail = typeof data?.detail === "string" ? data.detail : "Không thể hoàn tất yêu cầu.";
    const message = firstError
      ? `${fieldLabels[firstError.field] || "Dữ liệu"}: ${firstError.message}`
      : detail;
    throw new Error(message);
  }
  if (!data) throw new Error("API trả về dữ liệu không hợp lệ.");
  return data;
}

export const productApi = {
  list({ query, page, pageSize }) {
    const params = new URLSearchParams({ q: query, page: String(page), page_size: String(pageSize) });
    return request(`?${params}`);
  },
  get(id) { return request(`/${id}`); },
  create(data) { return request("", { method: "POST", body: JSON.stringify(data) }); },
  update(id, data) { return request(`/${id}`, { method: "PUT", body: JSON.stringify(data) }); },
  remove(id) { return request(`/${id}`, { method: "DELETE" }); },
};
