import {
  Calendar,
  CheckCircle,
  Box,
  Trophy,
  Plus,
  BarChart,
} from "lucide-react";

export default function Dashboard() {
  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold">Current Month Overview</h1>
        <p className="text-gray-600">Your progress for {new Date().toLocaleString('default', { month: 'long', year: 'numeric' })}</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

        {/* Items */}
        <div className="p-5 bg-white rounded-xl shadow-sm border border-gray-200">
          <div className="flex items-center justify-between">
            <h2 className="text-gray-700 font-semibold">Items</h2>
            <Box className="text-indigo-600" size={24} />
          </div>
          <p className="text-3xl font-bold mt-2">27</p>
          <p className="text-sm text-gray-500">Total items in this month</p>
        </div>

        {/* Completed */}
        <div className="p-5 bg-white rounded-xl shadow-sm border border-gray-200">
          <div className="flex items-center justify-between">
            <h2 className="text-gray-700 font-semibold">Completed</h2>
            <CheckCircle className="text-green-600" size={24} />
          </div>
          <p className="text-3xl font-bold mt-2">11</p>
          <p className="text-sm text-gray-500">Finished tasks</p>
        </div>

        {/* Sets */}
        <div className="p-5 bg-white rounded-xl shadow-sm border border-gray-200">
          <div className="flex items-center justify-between">
            <h2 className="text-gray-700 font-semibold">Sets</h2>
            <BarChart className="text-blue-600" size={24} />
          </div>
          <p className="text-3xl font-bold mt-2">5</p>
          <p className="text-sm text-gray-500">Active sets</p>
        </div>

        {/* Achievements */}
        <div className="p-5 bg-white rounded-xl shadow-sm border border-gray-200">
          <div className="flex items-center justify-between">
            <h2 className="text-gray-700 font-semibold">Achievements</h2>
            <Trophy className="text-yellow-500" size={24} />
          </div>
          <p className="text-3xl font-bold mt-2">3</p>
          <p className="text-sm text-gray-500">Unlocked this month</p>
        </div>

      </div>

      {/* Middle Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

        {/* Mini Calendar */}
        <div className="p-5 bg-white border border-gray-200 shadow-sm rounded-xl">
          <div className="flex items-center justify-between mb-3">
            <h2 className="font-semibold text-gray-700">This Month</h2>
            <Calendar size={20} className="text-indigo-600" />
          </div>
          <img
            src="https://i.imgur.com/7QJph9R.png"
            className="rounded-lg border border-gray-200"
            alt="Calendar placeholder"
          />
        </div>

        {/* Progress Section */}
        <div className="p-5 bg-white border border-gray-200 shadow-sm rounded-xl col-span-2">
          <h2 className="font-semibold text-gray-700 mb-4">Monthly Progress</h2>

          <div className="space-y-4">
            {/* Progress bar */}
            <div>
              <p className="text-sm text-gray-600 mb-1">Items Completed</p>
              <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-indigo-600 rounded-full"
                  style={{ width: "40%" }}
                ></div>
              </div>
            </div>

            <div>
              <p className="text-sm text-gray-600 mb-1">Sets Progress</p>
              <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-blue-500 rounded-full"
                  style={{ width: "60%" }}
                ></div>
              </div>
            </div>

            <div>
              <p className="text-sm text-gray-600 mb-1">Achievements</p>
              <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className="h-full bg-yellow-500 rounded-full"
                  style={{ width: "20%" }}
                ></div>
              </div>
            </div>
          </div>
        </div>

      </div>

      {/* Quick Actions */}
      <div className="p-5 bg-white border border-gray-200 shadow-sm rounded-xl">
        <h2 className="font-semibold text-gray-700 mb-4">Quick Actions</h2>

        <div className="flex gap-4">
          <button className="flex items-center space-x-2 bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700">
            <Plus size={18} />
            <span>Add Item</span>
          </button>

          <button className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
            <Plus size={18} />
            <span>Create Set</span>
          </button>

          <button className="flex items-center space-x-2 bg-yellow-600 text-white px-4 py-2 rounded-lg hover:bg-yellow-700">
            <Plus size={18} />
            <span>New Achievement</span>
          </button>
        </div>
      </div>

    </div>
  );
}
