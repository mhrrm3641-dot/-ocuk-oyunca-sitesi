import { useState } from 'react';
import Admin from './pages/Admin';
// ... diğer componentlerin

export default function App() {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <div>
      {/* Basit bir admin geçiş butonu (gizli bir yere koyabilirsin) */}
      <button onClick={() => setCurrentPage(currentPage === 'home' ? 'admin' : 'home')}>
        {currentPage === 'home' ? 'Yönetim Paneli' : 'Ana Sayfaya Dön'}
      </button>

      {currentPage === 'home' ? (
        <div>
           {/* Burası senin ana siten */}
           <h1>Siber Üs Ana Sayfa</h1>
        </div>
      ) : (
        <Admin />
      )}
    </div>
  );
}
