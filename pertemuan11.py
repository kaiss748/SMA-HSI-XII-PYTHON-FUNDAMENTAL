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


"""
Latihan 2: Hitung Rata-rata Spam Confidence
Gunakan file mbox-short.txt dari www.py4e.com/code3/mbox-short.txt.
Tulis program yang:
    1. Membaca file baris per baris.
    2. Mencari baris yang diawali dengan X-DSPAM-Confidence:.
    3. Untuk setiap baris yang cocok, ekstrak angka desimal di akhir baris tersebut.
    4. Hitung rata-rata dari semua angka yang berhasil diekstrak dan cetak hasilnya.
Petunjuk: Gunakan .startswith() dan slicing string. Konversi hasil slicing ke float.
"""
while True:
    input_file_2 = input("Masukan nama file (mbox-short.txt):")
    try:
        with open(input_file_2, 'r') as file2:
            total = 0
            jumlah = 0 # count -> menghitung berapa banyak angka desimalnya... misal [1,2,9,8], jumlahnya = 4

            for baris in file2:
                if baris.startswith("X-DSPAM-Confidence:"):
                    nilai = float(baris.strip()[20:])
                    total += nilai
                    jumlah += 1
                    print(f"decimal -> {nilai}")

            if jumlah>0:
                rata_rata = total / jumlah
                print(f"rata-rata -> {rata_rata}")

            else:
                print("tidak menemukan baris yang sesuai")

            break

    except FileNotFoundError:
        print("file tidak ditemukan")
        continue


"""
Latihan 3: Easter Egg File
Modifikasi program Latihan 1. Jika pengguna memasukkan nama file yang persis sama dengan "na na
boo boo", program tidak boleh mencoba membuka file tersebut, melainkan harus mencetak pesan lucu:
NA NA BOO BOO TO YOU - You have been punk'd! dan kemudian berhenti. Untuk semua input
nama file lainnya, program harus berjalan normal (dan menangani FileNotFoundError jika file tidak ada).
"""

while True:
    nama_file = input("Masukan nama file (puisi.txt): ")
    if nama_file == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        break
    try:
            
        with open(nama_file, 'r') as file:
            if nama_file == "puisi.txt":
                for baris in file:
                    print(baris.upper().strip())


            else :
                print("nama file invalid")
            break
                

    except FileNotFoundError:
        print("file tidak ditemukan")
        continue