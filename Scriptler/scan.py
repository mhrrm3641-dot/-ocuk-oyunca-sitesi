import socket

def port_tara(ip, port):
    # TCP bağlantısı oluşturmayı dener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # 1 saniye bekle, cevap gelmezse kapalı say
    
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port}: AÇIK")
    s.close()

hedef_ip = "127.0.0.1" # Kendi cihazımızı tarıyoruz
taranacak_portlar = [21, 22, 80, 443, 4444, 8080]

print(f"--- {hedef_ip} taranıyor ---")
for port in taranacak_portlar:
    port_tara(hedef_ip, port)

