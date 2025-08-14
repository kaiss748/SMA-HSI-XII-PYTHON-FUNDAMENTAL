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