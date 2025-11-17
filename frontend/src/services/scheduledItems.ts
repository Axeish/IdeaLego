export interface Schedule {
  id: string;
  itemId: string;
  setId?: string;
  month: string;
  startDate?: string;
  endDate?: string;
  repeat?: boolean;
  completed?: boolean;
  createdAt?: string;
  updatedAt?: string;
}

const BASE_URL = "http://127.0.0.1:8000/schedules";

export async function getSchedules(): Promise<Schedule[]> {
  const res = await fetch(BASE_URL + "/");
  if (!res.ok) throw new Error("Failed to fetch schedules");
  return res.json();
}

export async function createSchedule(schedule: Schedule): Promise<Schedule> {
  const res = await fetch(BASE_URL + "/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(schedule),
  });
  if (!res.ok) throw new Error("Failed to create schedule");
  return res.json();
}

export async function deleteSchedule(id: string): Promise<void> {
  const res = await fetch(`${BASE_URL}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete schedule");
}
