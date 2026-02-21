import { Outlet } from "react-router-dom";
import { NavLink } from "react-router-dom";
import { useAuthStore } from "@/store/authStore";

export function AdminLayout() {
  const logout = useAuthStore((s) => s.logout);

  return (
    <div className="flex min-h-screen">
      <aside className="w-64 bg-gray-900 text-white flex flex-col">
        <div className="px-6 py-5 text-xl font-bold border-b border-gray-700">
          🌿 Admin Panel
        </div>
        <nav className="flex-1 p-4 space-y-1">
          <NavLink to="/dashboard" className="block px-4 py-2 rounded hover:bg-gray-700">
            Dashboard
          </NavLink>
          <NavLink to="/users" className="block px-4 py-2 rounded hover:bg-gray-700">
            Пользователи
          </NavLink>
        </nav>
        <button
          onClick={logout}
          className="m-4 px-4 py-2 bg-red-600 rounded hover:bg-red-500 text-sm"
        >
          Выйти
        </button>
      </aside>
      <main className="flex-1 bg-gray-50 p-8">
        <Outlet />
      </main>
    </div>
  );
}
