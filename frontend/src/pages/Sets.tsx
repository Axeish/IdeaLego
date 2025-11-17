import { useEffect, useState } from "react";
import { getSets, createSet, deleteSet } from "../services/sets";
import type { Set } from "../services/sets";

export default function Sets() {
  const [sets, setSets] = useState<Set[]>([]);

  async function load() {
    const data = await getSets();
    setSets(data);
  }

  async function addTest() {
    await createSet({
      id: "set" + Date.now(),
      name: "New Test Set",
    });
    load();
  }

  async function remove(id: string) {
    await deleteSet(id);
    load();
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Sets</h1>
      <button onClick={addTest} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">+ Add Test Set</button>
      <ul className="space-y-2">
        {sets.map(s => (
          <li key={s.id} className="flex justify-between bg-gray-100 p-2 rounded">
            <span>{s.name}</span>
            <button onClick={() => remove(s.id)} className="text-red-600 font-bold">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
