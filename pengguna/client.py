import socket
import os
import time
import datetime

LOG_FILE = "client_log.txt"

def tulis_log(pesan):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{waktu}] {pesan}\n")

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

def koneksi_ke_server(ip, port):
    while True:
        try:
            tulis_log(f"Mencoba koneksi ke {ip}:{port}")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, port))
            s.settimeout(None)
            tulis_log(f"Berhasil koneksi ke {ip}:{port}")
            print(f"Berhasil koneksi ke {ip}:{port}")
            return s
        except Exception as e:
            tulis_log(f"Gagal koneksi ke {ip}:{port}. Error: {e}")
            print(f"Gagal koneksi ke {ip}:{port}. Error: {e}")
            print("Akan mencoba ulang dalam 5 detik...")
            time.sleep(5)

def main():
    ip = input_ip()
    port = input_port()
    s = koneksi_ke_server(ip, port)

    while True:
        clear_screen()
        try:
            menu = s.recv(1024).decode()
            print(menu)
            tulis_log(f"Menu diterima:\n{menu}")
            pilihan = input("Masukkan pilihan nomor: ").strip()
            s.sendall(pilihan.encode())
            tulis_log(f"Pilihan dikirim: {pilihan}")
            balasan = s.recv(1024).decode()
            print("Balasan dari server:", balasan)
            tulis_log(f"Balasan diterima: {balasan.strip()}")
            if pilihan == '8':
                print("ESP32 dimatikan. Program client keluar.")
                tulis_log("Client keluar karena shutdown (8).")
                break
            elif pilihan == '0':
                print("Keluar dari program client.")
                tulis_log("Client keluar karena pilihan (0).")
                break
            input("Tekan Enter untuk melanjutkan...")
        except Exception as e:
            tulis_log(f"Error komunikasi: {e}")
            print("Koneksi ke server terputus atau terjadi error:", e)
            print("Mencoba reconnect ke server...")
            try:
                s.close()
            except:
                pass
            s = koneksi_ke_server(ip, port)

    try:
        s.close()
    except:
        pass
    tulis_log("Client selesai dijalankan.")

if __name__ == "__main__":
    main()