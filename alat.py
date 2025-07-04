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

def led_morse_sos():
    global berkedip
    print("LED berkedip Morse SOS")
    morse = [0.1,0.1,0.1,0.3,0.3,0.3,0.1,0.1,0.1]
    while berkedip:
        for t in morse:
            lampu.off()
            sleep(t)
            lampu.on()
            sleep(0.1)
        sleep(1)  # jeda antarkode

def led_gradual():
    global berkedip
    print("LED berkedip gradual")
    while berkedip:
        for t in [0.5, 0.4, 0.3, 0.2, 0.1, 0.2, 0.3, 0.4]:
            lampu.off()
            sleep(t)
            lampu.on()
            sleep(t)

def lampu_led_gradual():
    global berkedip
    berkedip = False
    berkedip = True
    _thread.start_new_thread(led_gradual, ())

def lampu_led_morse_sos():
    global berkedip
    berkedip = False
    berkedip = True
    _thread.start_new_thread(led_morse_sos, ())

def lampu_led_acak():
    global berkedip
    berkedip = False
    berkedip = True
    _thread.start_new_thread(led_acak, ())

def lampu_led_cepat():
    global berkedip
    berkedip = False
    berkedip = True
    _thread.start_new_thread(led_cepat, ())

def lampu_led_lambat():
    global berkedip
    berkedip = False
    berkedip = True
    _thread.start_new_thread(led_lambat, ())

