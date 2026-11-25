import { productApi } from "./api.js";

const state = { query: "", page: 1, pageSize: 5, total: 0, editingId: null, loading: false, mutating: false, requestId: 0 };
const element = (id) => document.getElementById(id);
const form = element("product-form");
const priceFormat = new Intl.NumberFormat("vi-VN", { style: "currency", currency: "VND", maximumFractionDigits: 0 });

function notify(message, isError = false) {
  const notice = element("notice");
  notice.textContent = message;
  notice.classList.toggle("error", isError);
  notice.hidden = false;
}

function updateControls() {
  for (const field of form.querySelectorAll("input, textarea, button")) field.disabled = state.mutating;
  for (const button of document.querySelectorAll(".row-actions button")) button.disabled = state.mutating || state.loading;
  element("previous-button").disabled = state.loading || state.mutating || state.page <= 1;
  element("next-button").disabled = state.loading || state.mutating || state.page * state.pageSize >= state.total;
  element("reload-button").disabled = state.loading || state.mutating;
  element("save-button").textContent = state.mutating ? "Đang xử lý…" : (state.editingId ? "Lưu thay đổi" : "Lưu sản phẩm");
}

function resetForm() {
  state.editingId = null;
  form.reset();
  element("form-title").textContent = "Thêm sản phẩm";
  element("form-caption").textContent = "Nhập thông tin để tạo một sản phẩm mới.";
  element("reset-button").textContent = "Nhập lại";
  updateControls();
}

function showListState(title, description) {
  element("table-container").hidden = true;
  element("list-state").hidden = false;
  element("list-state-title").textContent = title;
  element("list-state-description").textContent = description;
}

function renderProducts(items) {
  const template = element("product-row-template");
  const rows = items.map((product) => {
    const row = template.content.firstElementChild.cloneNode(true);
    // Nội dung người dùng được gán bằng textContent, không chèn HTML.
    row.querySelector(".product-name").textContent = product.name;
    row.querySelector(".product-description").textContent = product.description || "Chưa có mô tả";
    row.querySelector(".product-id").textContent = `Mã #${product.id}`;
    row.querySelector(".product-price").textContent = priceFormat.format(product.price_vnd);
    const stock = row.querySelector(".stock-badge");
    stock.textContent = String(product.stock);
    stock.classList.toggle("empty-stock", product.stock === 0);
    const editButton = row.querySelector(".edit-button");
    const deleteButton = row.querySelector(".delete-button");
    editButton.setAttribute("aria-label", `Sửa ${product.name}`);
    deleteButton.setAttribute("aria-label", `Xóa ${product.name}`);
    editButton.addEventListener("click", () => editProduct(product.id));
    deleteButton.addEventListener("click", () => deleteProduct(product));
    return row;
  });
  element("product-rows").replaceChildren(...rows);
  element("list-state").hidden = true;
  element("table-container").hidden = false;
}

async function loadProducts() {
  const requestId = ++state.requestId;
  state.loading = true;
  element("product-total").textContent = "…";
  showListState("Đang tải dữ liệu…", "Đang lấy danh sách sản phẩm từ API.");
  updateControls();
  try {
    const data = await productApi.list(state);
    if (requestId !== state.requestId) return;
    const lastPage = Math.max(1, Math.ceil(data.total / state.pageSize));
    if (state.page > lastPage) {
      state.page = lastPage;
      await loadProducts();
      return;
    }
    state.total = data.total;
    element("product-total").textContent = String(data.total);
    element("page-label").textContent = `${state.page} / ${lastPage}`;
    const start = data.total === 0 ? 0 : (state.page - 1) * state.pageSize + 1;
    element("page-summary").textContent = `Hiển thị ${start}–${Math.min(state.page * state.pageSize, data.total)} / ${data.total} sản phẩm`;
    element("connection-status").textContent = "Đã kết nối API";
    element("connection-status").className = "connection connected";
    if (data.items.length) renderProducts(data.items);
    else showListState(state.query ? "Không tìm thấy sản phẩm" : "Chưa có sản phẩm nào", state.query ? "Thử tên khác hoặc xóa nội dung tìm kiếm." : "Thêm sản phẩm đầu tiên để bắt đầu quản lý.");
  } catch (error) {
    if (requestId !== state.requestId) return;
    state.total = 0;
    element("product-total").textContent = "—";
    element("page-summary").textContent = "Chưa tải được dữ liệu";
    element("connection-status").textContent = "Chưa kết nối được";
    element("connection-status").className = "connection disconnected";
    showListState("Không thể tải danh sách", error.message);
  } finally {
    if (requestId === state.requestId) {
      state.loading = false;
      updateControls();
    }
  }
}

async function editProduct(id) {
  state.mutating = true;
  updateControls();
  try {
    const product = await productApi.get(id);
    state.editingId = id;
    element("product-name").value = product.name;
    element("product-price").value = product.price_vnd;
    element("product-stock").value = product.stock;
    element("product-description").value = product.description;
    element("form-title").textContent = "Chỉnh sửa sản phẩm";
    element("form-caption").textContent = `Đang chỉnh sửa sản phẩm #${id}.`;
    element("reset-button").textContent = "Hủy chỉnh sửa";
    element("notice").hidden = true;
  } catch (error) {
    notify(error.message, true);
  } finally {
    state.mutating = false;
    updateControls();
    if (state.editingId === id) element("product-name").focus();
  }
}

async function deleteProduct(product) {
  if (!window.confirm(`Bạn muốn xóa sản phẩm “${product.name}”?`)) return;
  state.mutating = true;
  updateControls();
  try {
    await productApi.remove(product.id);
    if (state.editingId === product.id) resetForm();
    notify(`Đã xóa sản phẩm “${product.name}”.`);
    await loadProducts();
  } catch (error) {
    notify(error.message, true);
  } finally {
    state.mutating = false;
    updateControls();
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = {
    name: element("product-name").value.trim(),
    description: element("product-description").value.trim(),
    price_vnd: element("product-price").valueAsNumber,
    stock: element("product-stock").valueAsNumber,
  };
  if (!data.name) return notify("Tên sản phẩm không được chỉ chứa khoảng trắng.", true);
  if (!Number.isSafeInteger(data.price_vnd) || !Number.isSafeInteger(data.stock)) return notify("Giá bán và tồn kho phải là số nguyên.", true);
  const editingId = state.editingId;
  state.mutating = true;
  updateControls();
  try {
    if (editingId) await productApi.update(editingId, data);
    else await productApi.create(data);
    resetForm();
    if (!editingId) {
      state.page = 1;
      state.query = "";
      element("search-input").value = "";
    }
    notify(editingId ? "Đã lưu thay đổi sản phẩm." : "Đã thêm sản phẩm mới.");
    await loadProducts();
  } catch (error) {
    notify(error.message, true);
  } finally {
    state.mutating = false;
    updateControls();
  }
});

element("reset-button").addEventListener("click", resetForm);
element("reload-button").addEventListener("click", loadProducts);
element("search-form").addEventListener("submit", (event) => {
  event.preventDefault();
  state.query = element("search-input").value.trim();
  state.page = 1;
  loadProducts();
});
element("search-input").addEventListener("search", () => {
  if (element("search-input").value === "") {
    state.query = "";
    state.page = 1;
    loadProducts();
  }
});
element("previous-button").addEventListener("click", () => { state.page -= 1; loadProducts(); });
element("next-button").addEventListener("click", () => { state.page += 1; loadProducts(); });

loadProducts();
