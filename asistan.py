import json
import os
import os
import json

# Önce değişiklikleri kaydet ve senkronize et
os.system("git add .")
os.system('git commit -m "Asistan: Otomatik Guncelleme"')
os.system("git pull origin ana --rebase") 
os.system("git push origin ana")
print("Otomasyon tamamlandı!")

def veriyi_guncelle(yeni_baslik, yeni_icerik):
    # 1. veri.json dosyasını güncelle
    data = {
        "haberler": [{"baslik": yeni_baslik, "icerik": yeni_icerik}],
        "projeler": [{"ad": "Siber Asistan", "link": "#"}]
    }
    with open('veri.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Güncelleme yapıldı: {yeni_baslik}")
    
    # 2. Otomatik Git Otomasyonu
    print("GitHub'a gönderiliyor...")
    os.system("git add veri.json")
    os.system('git commit -m "Asistan: Veri guncellendi"')
    os.system("git push")
    print("Otomasyon tamamlandı. Site canlıda!")

if __name__ == "__main__":
    # Örnek kullanım: Burayı kendine göre değiştirebilirsin
    veriyi_guncelle("Yeni Haber Başlığı", "Siber Üs artık otomatik güncelleniyor.")
