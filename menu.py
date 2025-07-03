import alat

def get_menu():
    return (
        "=== MENU ESP32 ===\n"
        "1. Matikan lampu\n"
        "2. Nyalakan lampu\n"
        "3. Kedip cepat\n"
        "4. Kedip lambat\n"
        "5. Kedip acak\n"
        "6. Kedip Morse SOS\n"
        "7. Kedip gradual\n"
        "8. Shutdown ESP32\n"
        "0. Keluar\n"
        "Pilih nomor: "
    )

def proses_pilihan(pilihan, alat):
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
        alat.lampu_led_acak()
        return 'Lampu berkedip acak\n'
    elif pilihan == '6':
        alat.lampu_led_morse_sos()
        return 'Lampu berkedip Morse SOS\n'
    elif pilihan == '7':
        alat.lampu_led_gradual()
        return 'Lampu berkedip gradual\n'
    elif pilihan == '8':
        alat.mati()
        return 'ESP32 akan dimatikan.\n'
    elif pilihan == '0':
        return 'Keluar. Terima kasih!\n'
    else:
        return 'Pilihan tidak dikenal, coba lagi.\n'