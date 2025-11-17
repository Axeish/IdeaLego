import { useEffect, useState } from "react";
import { getAchievements, createAchievement, deleteAchievement } from "../services/achievements";
import type { Achievement } from "../services/achievements";

export default function Achievements() {
  const [achievements, setAchievements] = useState<Achievement[]>([]);

  async function load() {
    const data = await getAchievements();
    setAchievements(data);
  }

  async function addTest() {
    await createAchievement({
      id: "ach" + Date.now(),
      title: "New Test Achievement",
    });
    load();
  }

  async function remove(id: string) {
    await deleteAchievement(id);
    load();
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Achievements</h1>
      <button onClick={addTest} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">+ Add Test Achievement</button>
      <ul className="space-y-2">
        {achievements.map(a => (
          <li key={a.id} className="flex justify-between bg-gray-100 p-2 rounded">
            <span>{a.title}</span>
            <button onClick={() => remove(a.id)} className="text-red-600 font-bold">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
