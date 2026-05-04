import hashlib

# Kırmak istediğimiz hedef hash (Bu "sifre123" kelimesinin hash'idir)
hedef_hash = "642967ce9745d27f8a70f2824b42f6236b32c66c30335831969e6b4f71589412"

# Denenecek şifreler listesi (Sözlük)
sozluk = ["admin", "123456", "muharrem", "sifre123", "password"]

for kelime in sozluk:
    # Listedeki kelimeyi hash'le
    deneme = hashlib.sha256(kelime.encode()).hexdigest()
    
    if deneme == hedef_hash:
        print(f"BULDUM! Şifre şudur: {kelime}")
        break
else:
    print("Sözlükte eşleşen bir şifre bulunamadı.")

