"""
Latihan 2: Salin File
Buat program yang menyalin isi dari satu file ke file lain.
    1. Buat file sumber bernama sumber.txt dan isi dengan beberapa baris teks.
    2. Program harus membuka sumber.txt dalam mode baca ('r').
    3. Program harus membuka file tujuan bernama salinan.txt dalam mode tulis ('w').
    4. Baca isi dari sumber.txt (bisa dengan .read() karena kita menyalin semuanya) dan tulis ke
salinan.txt.
"""

sumber = "sumber.txt"
tujuan = "salinan.txt"

with open(sumber, 'r') as file_sumber: # -> membuka file sumber untuk membaca
    isi = file_sumber.read()
    print(isi)

with open(tujuan, 'w') as file_tujuan:
    file_tujuan.write(isi)

print(f"file '{sumber}' berhasil disalin ke '{tujuan}'")