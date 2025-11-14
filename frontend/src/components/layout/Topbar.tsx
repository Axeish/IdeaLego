import { Bell, User } from "lucide-react";

export default function Topbar() {
  return (
    <div className="h-16 bg-white border-b border-gray-200 px-6 flex items-center justify-between">
      <h2 className="font-semibold text-lg">IdeaLego</h2>

      <div className="flex items-center space-x-4">
        <Bell size={20} className="text-gray-600" />
        <User size={20} className="text-gray-600" />
      </div>
    </div>
  );
}
