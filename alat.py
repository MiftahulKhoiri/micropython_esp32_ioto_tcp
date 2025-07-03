from machine import Pin
from time import sleep
from wifi import *
import _thread
import urandom


# Set pin lampu sesuai hardware (misal D2 = GPIO2)
LAMP_PIN = 2
lampu = Pin(LAMP_PIN, Pin.OUT)

# FLAG GLOBAL untuk kontrol thread LED
berkedip = False

def matikan_lampu():
    global berkedip
    berkedip = False   # Hentikan thread kedip
    lampu.off()        # Matikan lampu secara fisik
    print("Lampu dimatikan dan kedip dihentikan")

def nyalakan_lampu():
    global berkedip
    berkedip = False   # Pastikan kedip juga berhenti jika nyalakan manual
    lampu.on()
    print("Lampu dinyalakan")

def mati():
    print("Mematikan esp32")
    disconnect_wifi()

def led_cepat():
    global berkedip
    print("LED berkedip cepat")
    while berkedip:
        lampu.off()
        sleep(0.1)
        lampu.on()
        sleep(0.1)

def led_lambat():
    global berkedip
    print("LED berkedip lambat")
    while berkedip:
        lampu.off()
        sleep(0.5)
        lampu.on()
        sleep(0.5)


def led_acak():
    global berkedip
    print("LED berkedip acak")
    while berkedip:
        lampu.off()
        sleep(urandom.uniform(0.05, 0.5))
        lampu.on()
        sleep(urandom.uniform(0.05, 0.5))



def lampu_led_acak():
    global berkedip
    berkedip = True
    _thread.start_new_thread(led_acak, ())

def lampu_led_cepat():
    global berkedip
    berkedip = True
    _thread.start_new_thread(led_cepat, ())

def lampu_led_lambat():
    global berkedip
    berkedip = True
    _thread.start_new_thread(led_lambat, ())

