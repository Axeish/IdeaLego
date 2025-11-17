import { useEffect, useState } from "react";
import { getItems, createItem, deleteItem } from "../services/items";
import type { Item } from "../services/items"; // <-- import type only

export default function Items() {
  const [items, setItems] = useState<Item[]>([]);

  async function load() {
    const data = await getItems();
    setItems(data);
  }

  async function addTest() {
    await createItem({
      id: "demo" + Date.now(),
      name: "New Test Item",
    });
    load();
  }

  async function remove(id: string) {
    await deleteItem(id);
    load();
  }

  useEffect(() => {
    load();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Items</h1>

      <button
        onClick={addTest}
        className="bg-blue-600 text-white px-4 py-2 rounded mb-4"
      >
        + Add Test Item
      </button>

      <ul className="space-y-2">
        {items.map((i) => (
          <li
            key={i.id}
            className="flex justify-between bg-gray-100 p-2 rounded"
          >
            <span>{i.name}</span>
            <button
              onClick={() => remove(i.id)}
              className="text-red-600 font-bold"
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
