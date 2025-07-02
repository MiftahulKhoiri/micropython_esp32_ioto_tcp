import socket
import alat

PORT = 661

def get_menu():
    return (
        "=== MENU ESP32 ===\n"
        "1. Matikan lampu\n"
        "2. Nyalakan lampu\n"
        "3. Kedip cepat\n"
        "4. Kedip lambat\n"
        "5. Shutdown ESP32\n"
        "0. Keluar\n"
        "Pilih nomor: "
    )

def proses_pilihan(pilihan, alat):
    # alat adalah modul/fungsi yang diimport dari alat.py
    if pilihan == '1':
        alat.matikan_lampu()
        return 'Lampu dimatikan\n'
    elif pilihan == '2':
        alat.nyalakan_lampu()
        return 'Lampu dinyalakan\n'
    elif pilihan == '3':
        alat.lampu_led_cepat()
        return 'Lampu berkedip cepat\n'
    elif pilihan == '4':
        alat.lampu_led_lambat()
        return 'Lampu berkedip lambat\n'
    elif pilihan == '5':
        alat.mati()
        return 'ESP32 akan dimatikan.\n'
    elif pilihan == '0':
        return 'Keluar. Terima kasih!\n'
    else:
        return 'Pilihan tidak dikenal, coba lagi.\n'

def webserver():
    addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Menunggu koneksi di port', PORT)

    while True:
        try:
            cl, addr_client = s.accept()
            print('Client terhubung dari', addr_client)
            while True:
                cl.send(get_menu().encode())
                pilihan = cl.recv(1024).decode().strip()
                print('Pilihan:', pilihan)
                balasan = proses_pilihan(pilihan, alat)
                cl.send(balasan.encode())
                if pilihan == '5' or pilihan == '0':
                    cl.close()
                    break
        except Exception as e:
            print("Error:", e)