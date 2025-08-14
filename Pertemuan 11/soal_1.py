"""
Latihan 1: Tampilkan Semua Uppercase
Buat file puisi.txt. Tulis program yang:
    1. Meminta pengguna memasukkan nama file (puisi.txt).
    2. Membaca file tersebut baris per baris.
    3. Mencetak setiap baris ke layar dalam format HURUF KAPITAL SEMUA.
"""
while True:
    nama_file = input("Masukan nama file (puisi.txt): ")
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                print(baris.upper().strip())
            break

    except FileNotFoundError:
        print("file tidak ditemukan")
        continue
