import React, { useState } from 'react';

export default function App() {
  const [isAdmin, setIsAdmin] = useState(false);
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    if (password === 'siber123') setIsAdmin(true);
    else alert('Yetkisiz Giriş!');
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>GLOBAL CYBER BASE</h1>
      
      {isAdmin ? (
        <div style={{ border: '2px solid red', padding: '20px' }}>
          <h2>🛠 YÖNETİM PANELİ AKTİF</h2>
          <button onClick={() => setIsAdmin(false)}>KİLİTLE</button>
        </div>
      ) : (
        <button onClick={handleLogin}>
          <input type="password" onChange={(e) => setPassword(e.target.value)} placeholder="Şifre" />
          Giriş Yap
        </button>
      )}
    </div>
  );
}
