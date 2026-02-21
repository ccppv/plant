export function DashboardPage() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-white shadow rounded p-6">
          <p className="text-gray-500 text-sm">Всего пользователей</p>
          <p className="text-3xl font-bold text-gray-800">—</p>
        </div>
        <div className="bg-white shadow rounded p-6">
          <p className="text-gray-500 text-sm">Активных сегодня</p>
          <p className="text-3xl font-bold text-gray-800">—</p>
        </div>
        <div className="bg-white shadow rounded p-6">
          <p className="text-gray-500 text-sm">Растений в БД</p>
          <p className="text-3xl font-bold text-gray-800">—</p>
        </div>
      </div>
    </div>
  );
}
