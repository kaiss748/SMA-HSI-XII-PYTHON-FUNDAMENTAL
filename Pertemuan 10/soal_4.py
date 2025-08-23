"""
Latihan 4: Akronim Generator
Buat program yang meminta pengguna memasukkan sebuah nama organisasi yang panjang (misal: "Badan
Usaha Milik Negara"). Program harus:
    1. Memecah input menjadi list kata-kata.
    2. Mengambil huruf pertama dari setiap kata.
    3. Menggabungkan huruf-huruf pertama tersebut menjadi satu string akronim dalam huruf kapital.
Output yang diharapkan: "BUMN"
"""

#CARA RIBET
nama_organisasi = input("Masukan nama lembaga : ")
bagian_nama = nama_organisasi.split()
kata_pertama = bagian_nama[0]
huruf_pertama = kata_pertama[0]

kata_kedua = bagian_nama[1]
huruf_kedua = kata_kedua[0]

kata_ketiga = bagian_nama[2]
huruf_ketiga = kata_ketiga[0]

kata_keempat = bagian_nama[3]
huruf_keempat = kata_keempat[0]
singkatan = [huruf_pertama, huruf_kedua, huruf_ketiga, huruf_keempat]
singkatan_valid = "".join(singkatan).upper()
print(singkatan_valid)

#CARA SIMPLE
nama_organisasi = input("Masukkan nama lembaga: ")
bagian_nama = nama_organisasi.split()

singkatan = "" #Inisialisasi string kosong untuk menampung huruf awal tiap kata
for kata in bagian_nama: # Loop untuk mengambil huruf pertama dari setiap kata
    singkatan += kata[0]

print(singkatan.upper())