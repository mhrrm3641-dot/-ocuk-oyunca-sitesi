import time
import os

# İzlemek istediğimiz dosya veya durum
izlenecek_dosya = "/data/data/com.termux/files/home/.bashrc"

def log_yaz(mesaj):
    with open("guvenlik_gunlugu.txt", "a") as f:
        f.write(f"[{time.ctime()}] - {mesaj}\n")

print("--- Güvenlik Gözlemcisi Başlatıldı ---")
log_yaz("Sistem izleme başlatıldı.")

try:
    son_degisim = os.path.getmtime(izlenecek_dosya)
    while True:
        su_anki_degisim = os.path.getmtime(izlenecek_dosya)
        if su_anki_degisim != son_degisim:
            print("! UYARI: .bashrc dosyası değiştirildi !")
            log_yaz("KRİTİK: .bashrc dosyasında değişiklik tespit edildi!")
            son_degisim = su_anki_degisim
        time.sleep(5) # 5 saniyede bir kontrol et
except KeyboardInterrupt:
    print("\nGözlemci durduruldu.")

