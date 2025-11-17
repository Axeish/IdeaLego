// frontend/src/services/achievements.ts
export interface Achievement {
  id: string;
  itemId?: string;
  setId?: string;
  categoryId?: string;
  month: string;
  completedAt?: string;
}

const BASE_URL = "http://127.0.0.1:8000/achievements";

export async function getAchievements(): Promise<Achievement[]> {
  const res = await fetch(`${BASE_URL}/`);
  if (!res.ok) throw new Error("Failed to fetch achievements");
  return res.json();
}

export async function createAchievement(ach: Achievement): Promise<Achievement> {
  const res = await fetch(`${BASE_URL}/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(ach),
  });
  if (!res.ok) throw new Error("Failed to create achievement");
  return res.json();
}

export async function deleteAchievement(id: string): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete achievement");
}
