import socket
import alat
from menu import *

PORT = 661

def webserver():
    addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Menunggu koneksi di port', PORT)

    try:
        while True:
            cl = None
            try:
                cl, addr_client = s.accept()
                print('Client terhubung dari', addr_client)
                while True:
                    cl.send(get_menu().encode())
                    pilihan = cl.recv(1024).decode().strip()
                    print('Pilihan:', pilihan)
                    balasan = proses_pilihan(pilihan, alat)
                    cl.send((balasan + "\n").encode())
                    # Shutdown (8) atau keluar (0) akan menutup koneksi
                    if pilihan == '8' or pilihan == '0':
                        cl.close()
                        break
            except Exception as e:
                print("Error:", e)
                if cl:
                    cl.close()
    finally:
        s.close()

if __name__ == "__main__":
    webserver()