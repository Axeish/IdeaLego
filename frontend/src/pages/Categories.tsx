import { useEffect, useState } from "react";
import { getCategories, createCategory, deleteCategory } from "../services/categories";
import type { Category } from "../services/categories";

export default function Categories() {
  const [categories, setCategories] = useState<Category[]>([]);

  async function load() {
    const data = await getCategories();
    setCategories(data);
  }

  async function addTest() {
    await createCategory({
      id: "cat" + Date.now(),
      name: "New Test Category",
    });
    load();
  }

  async function remove(id: string) {
    await deleteCategory(id);
    load();
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Categories</h1>
      <button onClick={addTest} className="bg-blue-600 text-white px-4 py-2 rounded mb-4">+ Add Test Category</button>
      <ul className="space-y-2">
        {categories.map(c => (
          <li key={c.id} className="flex justify-between bg-gray-100 p-2 rounded">
            <span>{c.name}</span>
            <button onClick={() => remove(c.id)} className="text-red-600 font-bold">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
