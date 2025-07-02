from wifi import *
from time import sleep
import socket
import server

def main ():
    connect_wifi()
    print ("menyalakan server")
    sleep(2)
    server.webserver()
    
if __name__ == '__main__':
    main()