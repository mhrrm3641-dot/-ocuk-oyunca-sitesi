import { useState } from "react";

export default function Admin() {
  const [password, setPassword] = useState("");
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = () => {
    if (password === "KENDI_SIFREN") { // Buraya kendine özel bir şifre koy
      setIsAuthenticated(true);
    }
  };

  if (!isAuthenticated) {
    return (
      <div className="flex flex-col items-center justify-center h-screen">
        <input type="password" onChange={(e) => setPassword(e.target.value)} className="border p-2" />
        <button onClick={handleLogin} className="bg-blue-500 text-white p-2 mt-2">Giriş Yap</button>
      </div>
    );
  }

  return (
    <div className="p-8">
      <h1>Siber Üs Kontrol Paneli</h1>
      {/* Buraya form gelecek, haber başlığı ve görsel yolu girilecek */}
    </div>
  );
}
