import { useEffect, useState } from "react";
import { getSchedules, createSchedule, deleteSchedule } from "../services/scheduledItems";
import type { Schedule } from "../services/scheduledItems";

export default function Schedules() {
  const [schedules, setSchedules] = useState<Schedule[]>([]);

  async function load() {
    const data = await getSchedules();
    setSchedules(data);
  }

  async function addTest() {
    await createSchedule({
      id: "sched" + Date.now(),
      title: "New Test Schedule",
    });
    load();
  }

  async function remove(id: string) {
    await deleteSchedule(id);
    load();
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Schedules</h1>
      <button onClick={addTest} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">+ Add Test Schedule</button>
      <ul className="space-y-2">
        {schedules.map(s => (
          <li key={s.id} className="flex justify-between bg-gray-100 p-2 rounded">
            <span>{s.title}</span>
            <button onClick={() => remove(s.id)} className="text-red-600 font-bold">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
