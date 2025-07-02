import socket
import os

def clear_screen():
    try:
        os_name = os.name
    except AttributeError:
        os_name = None

    if os_name == 'nt':
        os.system('cls')
    elif os_name == 'posix':
        os.system('clear')
    else:
        print('\n' * 100)

def input_ip():
    while True:
        ip = input("Masukkan alamat IP ESP32: ").strip()
        # Cek format IP sederhana
        parts = ip.split('.')
        if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
            return ip
        print("Alamat IP tidak valid! Silakan coba lagi.")

def input_port():
    while True:
        port_str = input("Masukkan port ESP32: ").strip()
        if port_str.isdigit():
            port = int(port_str)
            if 1 <= port <= 65535:
                return port
            else:
                print("Port harus di antara 1 dan 65535!")
        else:
            print("Port harus berupa angka! Silakan coba lagi.")

def main():
    while True:
        ip = input_ip()
        port = input_port()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # timeout 5 detik
            s.connect((ip, port))
            s.settimeout(None)
            break
        except Exception as e:
            print(f"Gagal koneksi ke {ip}:{port}. Error: {e}")
            print("Silakan masukkan ulang alamat IP dan port!\n")

    while True:
        clear_screen()
        try:
            menu = s.recv(1024).decode()
            print(menu)
            pilihan = input("Masukkan pilihan nomor: ").strip()
            s.sendall(pilihan.encode())
            balasan = s.recv(1024).decode()
            print("Balasan dari server:", balasan)
            if pilihan == '5':  # shutdown
                print("ESP32 dimatikan. Program client keluar.")
                break
            elif pilihan == '0':  # keluar
                print("Keluar dari program client.")
                break
            input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            print("Terjadi error komunikasi:", e)
            break
    s.close()

if __name__ == "__main__":
    main()