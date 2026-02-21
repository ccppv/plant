export function HomePage() {
  const tg = window.Telegram?.WebApp;
  const user = tg?.initDataUnsafe?.user;

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">🌿 Plant Tracker</h1>
      {user && (
        <p className="text-gray-600">
          Привет, {user.first_name}! Manage your plants here.
        </p>
      )}
      <div className="bg-green-50 rounded-xl p-4 border border-green-200">
        <p className="text-green-800">Ваши растения появятся здесь</p>
      </div>
    </div>
  );
}
