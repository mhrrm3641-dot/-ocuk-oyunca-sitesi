import time

# Sadece bu IP adreslerine izin veriliyor (Senin güvenli cihazların)
beyaz_liste = ["192.168.1.10", "127.0.0.1", "10.0.2.15"]

def baglanti_kontrol(gelen_ip):
    print(f"\n--- Yeni bağlantı isteği: {gelen_ip} ---")
    time.sleep(1) # Analiz ediliyormuş gibi bekleme süresi
    
    if gelen_ip in beyaz_liste:
        print(f"BEYAZ LİSTEDE: Erişim izni verildi. Hoş geldin {gelen_ip}!")
    else:
        print(f"!!! UYARI !!!: {gelen_ip} beyaz listede değil! BAĞLANTI REDDEDİLDİ.")

# Simülasyon
baglanti_kontrol("127.0.0.1")    # Bu senin kendi cihazın
baglanti_kontrol("185.22.41.9")  # Bu tanımadığın yabancı bir IP

