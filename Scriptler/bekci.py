import socket
import time

# İzlenecek cihaz ve portlar
hedef_ip = "192.168.1.1"
izlenecek_portlar = [80, 443, 52869]

# Alarmı dosyaya yazan fonksiyon
def log_kaydet(mesaj):
    with open("siber_us_log.txt", "a") as log_dosyasi:
        log_dosyasi.write(f"{time.ctime()}: {mesaj}\n")

print("--- SİBER ÜS BEKÇİSİ AKTİF (LOG KAYDI AÇIK) ---")

durumlar = {port: False for port in izlenecek_portlar}

while True:
    for port in izlenecek_portlar:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        yeni_durum = (s.connect_ex((hedef_ip, port)) == 0)
        
        if yeni_durum != durumlar[port]:
            if yeni_durum:
                mesaj = f"[!] ALARM: {port} portu AÇILDI!"
            else:
                mesaj = f"[!] BİLGİ: {port} portu KAPANDI."
            
            print(mesaj)
            log_kaydet(mesaj)
            durumlar[port] = yeni_durum
            
        s.close()
    
    time.sleep(30)

