// frontend/src/services/sets.ts
export interface Set {
  id: string;
  name: string;
  categoryId?: string;
  month?: string;
  progress?: number;
  createdAt?: string;
  updatedAt?: string;
}

const BASE_URL = "http://127.0.0.1:8000/sets";

export async function getSets(): Promise<Set[]> {
  const res = await fetch(`${BASE_URL}/`);
  if (!res.ok) throw new Error("Failed to fetch sets");
  return res.json();
}

export async function createSet(set: Set): Promise<Set> {
  const res = await fetch(`${BASE_URL}/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(set),
  });
  if (!res.ok) throw new Error("Failed to create set");
  return res.json();
}

export async function deleteSet(id: string): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete set");
}
