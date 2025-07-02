import network
import time
from machine import Pin

# Variabel global agar mudah diubah
SSID = 'baguschoiri'
PASSWORD = '12345678'
LED_PIN = 2  # GPIO2 umum untuk LED pada ESP32 (ganti jika berbeda)

# Inisialisasi LED
led = Pin(LED_PIN, Pin.OUT)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Menghubungkan ke jaringan WiFi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            led.value(0)  # LED mati saat belum konek
            time.sleep(0.5)
            led.value(1)
            time.sleep(0.5)
        print('Berhasil terhubung ke WiFi!')
        led.value(1)  # LED nyala saat sudah konek
        print('Alamat IP:', wlan.ifconfig()[0])
    else:
        print('Sudah terkoneksi, IP:', wlan.ifconfig()[0])
        led.value(1)
    return wlan

def disconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    led.value(0)
    print('WiFi diputus.')

def status_wifi():
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()

def get_ip():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        return wlan.ifconfig()[0]
    else:
        return None

# Jika ingin testing langsung:
if __name__ == '__main__':
    connect_wifi()