# Dosya adını belirt
dosya_adi = "rapor_192_168_1_1.txt"

print("--- SİBER ÜS RAPOR ANALİZİ ---")

# Dosyayı oku ve kontrol et
try:
    with open(dosya_adi, "r") as dosya:
        icerik = dosya.read()
        if "open" in icerik:
            print("[!] DİKKAT: Cihazda açık portlar tespit edildi.")
            for satir in icerik.splitlines():
                if "/tcp" in satir and "open" in satir:
                    print(f"Tespit edilen servis: {satir}")
        else:
            print("[+] Cihaz temiz görünüyor.")
except FileNotFoundError:
    print(f"Hata: {dosya_adi} dosyası bulunamadı. Önce tarama yapmalısın.")

