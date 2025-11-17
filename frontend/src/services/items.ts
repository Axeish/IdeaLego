export interface Item {
  id: string;
  name: string;
  description?: string;
  categoryId?: string;
  status?: string;
  priority?: number;
  tags?: string;
  deadline?: string;
  createdAt?: string;
  updatedAt?: string;
}

const BASE_URL = "http://127.0.0.1:8000/items";

export async function getItems(): Promise<Item[]> {
  const res = await fetch(BASE_URL + "/");
  if (!res.ok) throw new Error("Failed to fetch items");
  return res.json();
}

export async function createItem(item: Item): Promise<Item> {
  const res = await fetch(BASE_URL + "/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  if (!res.ok) throw new Error("Failed to create item");
  return res.json();
}

export async function deleteItem(id: string): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete item");
}
