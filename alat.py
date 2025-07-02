from machine import Pin
from time import sleep
from wifi import *

# Set pin lampu sesuai hardware (misal D2 = GPIO2)
LAMP_PIN = 2
lampu = Pin(LAMP_PIN, Pin.OUT)

def matikan_lampu():
    lampu.onff()
    print("Lampu dimatikan")

def nyalakan_lampu():
    lampu.on()
    print("Lampu dinyalakan")
 
def mati():
    print("Mematikan esp32")
    disconnect_wifi()

def lampu_led_cepat(jumlah_kedip=5):
    print("LED berkedip cepat")
    for i in range(jumlah_kedip):
        lampu.off()
        sleep(0.1)
        lampu.on()
        sleep(0.1)
        Lampu.off()
        sleep(0.1)

def lampu_led_lambat(jumlah_kedip=5):
    print("LED berkedip lambat")
    for i in range(jumlah_kedip):
        lampu.off()
        sleep(0.5)
        lampu.on()
        sleep(0.5)
        Lampu.off()
        sleep(0.5)