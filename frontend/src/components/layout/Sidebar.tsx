import { NavLink } from "react-router-dom";
import {
  LayoutGrid,
  Calendar,
  Box,
  Puzzle,
  Trophy,
  Tags,
  Menu,
} from "lucide-react";
import { useState } from "react";

export default function Sidebar() {
  const [open, setOpen] = useState(true);

  const menuItems = [
    { label: "Dashboard", icon: <LayoutGrid size={20} />, to: "/" },
    { label: "Schedule", icon: <Calendar size={20} />, to: "/schedule" },
    { label: "Sets", icon: <Box size={20} />, to: "/sets" },
    { label: "Items", icon: <Puzzle size={20} />, to: "/items" },
    { label: "Achievements", icon: <Trophy size={20} />, to: "/achievements" },
    { label: "Categories", icon: <Tags size={20} />, to: "/categories" },
  ];

  return (
    <div
      className={`h-screen bg-gray-900 text-white transition-all duration-300
        ${open ? "w-64" : "w-20"} flex flex-col`}
    >
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b border-gray-800">
        {open && <h1 className="font-bold text-xl">IdeaLego</h1>}
        <button onClick={() => setOpen(!open)}>
          <Menu size={22} />
        </button>
      </div>

      {/* Menu */}
      <nav className="flex-1 p-2 space-y-2">
        {menuItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `flex items-center space-x-3 p-3 rounded-lg transition
              ${isActive ? "bg-indigo-600" : "hover:bg-gray-800"}`
            }
          >
            {item.icon}
            {open && <span>{item.label}</span>}
          </NavLink>
        ))}
      </nav>
    </div>
  );
}
