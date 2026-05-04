def siteyi_guncelle():
    # Proje klasörüne git ve işlemleri yap
    print("\n[!] Web sitesi güncelleniyor...")
    os.chdir("os.chdir("/data/data/com.termux/files/home/siber_goz_app")

    os.system("git add .")
    os.system('git commit -m "Asistan: Otomatik Guncelleme"')
    os.system("git push")
    os.chdir("/data/data/com.termux/files/home") # Ana dizine geri dön
    print("[+] Site güncellendi!")

