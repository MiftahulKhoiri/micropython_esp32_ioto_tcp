import socket
import os

def clear_screen():
    # Cek jika berjalan di MicroPython (umumnya tidak ada os.name)
    try:
        os_name = os.name
    except AttributeError:
        os_name = None

    if os_name == 'nt':
        os.system('cls')
    elif os_name == 'posix':
        os.system('clear')
    else:
        # fallback, print banyak baris kosong
        print('\n' * 100)

def main():
    ip = input("Masukkan alamat IP ESP32: ").strip()
    port = int(input("Masukkan port ESP32: ").strip())
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        while True:
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
        s.close()
    except Exception as e:
        print("Gagal koneksi atau terjadi error:", e)

if __name__ == "__main__":
    main()