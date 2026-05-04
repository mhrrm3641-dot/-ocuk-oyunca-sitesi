import os
import shutil
import time

def sistem_temizle():
    print("\n[*] Gecici dosyalar temizleniyor...")
    # Gereksiz nano kayıtlarını ve geçici dosyaları siler
    if os.path.exists("Gecici"):
        for f in os.listdir("Gecici"):
            os.remove(os.path.join("Gecici", f))
    os.system("rm -f .*.swp *.save")
    print("[+] Temizlik tamam.")

def siteyi_guncelle():
    print("\n[!] Global Cyber Base guncelleniyor...")
    os.system("git add .")
    # Otomatik commit mesajına o anki saati ekleyelim
    saat = time.strftime('%H:%M:%S')
    os.system(f'git commit -m "Asistan Guncellemesi - {saat}"')
    os.system("git push origin master")
    print("[+] Site canliya alindi!")

def ana_menu():
    while True:
        os.system('clear')
        print("================================")
        print("   SIBER ASISTAN | MONITOR V1   ")
        print("================================")
        print("[1] Manuel Site Guncelle (Push)")
        print("[2] Sistem Temizliği Yap")
        print("[3] OTOMATIK MOD (Sürekli Takip)")
        print("[0] Çıkış")
        
        secim = input("\nKomut Bekleniyor: ")
        
        if secim == "1":
            siteyi_guncelle()
            input("\nDevam etmek icin Enter...")
        elif secim == "2":
            sistem_temizle()
            input("\nDevam etmek icin Enter...")
        elif secim == "3":
            print("[!] Otomatik mod aktif. (Cikis icin Ctrl+C)")
            try:
                while True:
                    sistem_temizle()
                    siteyi_guncelle()
                    print(f"[{time.strftime('%H:%M:%S')}] Beklemede...")
                    time.sleep(3600) # 1 saatte bir calisir
            except KeyboardInterrupt:
                print("\n[!] Otomatik mod durduruldu.")
        elif secim == "0":
            break

if __name__ == "__main__":
    ana_menu()

