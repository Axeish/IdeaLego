import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppLayout from "./components/layout/AppLayout";

import Dashboard from "./pages/Dashboard";
import Schedule from "./pages/Schedule";
import Sets from "./pages/Sets";
import Items from "./pages/Items";
import Achievements from "./pages/Achievements";
import Categories from "./pages/Categories";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* All pages share the sidebar + topbar */}
        <Route element={<AppLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/schedule" element={<Schedule />} />
          <Route path="/sets" element={<Sets />} />
          <Route path="/items" element={<Items />} />
          <Route path="/achievements" element={<Achievements />} />
          <Route path="/categories" element={<Categories />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
