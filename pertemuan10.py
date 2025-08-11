"""
Latihan 1: Standarisasi Judul
Buat program yang meminta pengguna memasukkan judul buku yang mungkin diketik dengan huruf
besar/kecil yang acak (misal: "aLaDiN dan LaMPu aJAib"). Programmu
"""

judul = input("Masukan judul : ")
final_judul = judul.strip().title()
print(final_judul)

"""
Latihan 2: Validasi Email Sederhana
Buat program yang meminta pengguna memasukkan alamat email. Program harus melakukan dua
pengecekan sederhana:
    1. Apakah email mengandung karakter @? (Gunakan find() atau operator in).
    2. Apakah email diakhiri dengan .com atau .co.id? (Gunakan .endswith()).
Cetak pesan "Email valid" atau "Email tidak valid" berdasarkan hasil pengecekan.
"""

email = input("Masukan email : ")
cek_1 = email.find("@") 
if (cek_1>=0) and (email.endswith(".com") or email.endswith(".co.id")):
    print("Nice dude, email lu valid!")
else:
    print("Nah dude, email lu ga valid!")


"""
Latihan 3: Sensor Kata
Buat program yang memiliki sebuah kalimat dan sebuah kata yang ingin disensor. Program harus mengganti
semua kemunculan kata terlarang itu dengan tanda bintang ***.
    Contoh: kalimat = "Harga tiketnya sangat mahal.", kata_sensor = "mahal".
    Output yang diharapkan: "Harga tiketnya sangat ***."
"""

kalimat = "Kalau jalan hati-hati bodoh"
kalimat_sensor = "bodoh"
kalimat_valid = kalimat.replace(kalimat_sensor, "***")
print(f"kalimat tdk baik =\n {kalimat}")
print(f"kalimat baik =\n {kalimat_valid}")
print(kalimat_valid)

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


"""
Latihan 5: URL Slug Generator
Di dunia web, "slug" adalah versi URL-friendly dari sebuah judul artikel. Buat program yang mengubah judul
artikel menjadi slug. Aturannya:
    1. Ubah semua huruf menjadi kecil.
    2. Ganti semua spasi dengan tanda hubung (-).
    3. (Bonus) Hapus semua karakter selain huruf, angka, dan tanda hubung.
Contoh: judul = "10 Tips Jitu Belajar Python!"
Output yang diharapkan: "10-tips-jitu-belajar-python"
"""

judul_artikel = input("Masukan judul artikel : ")
slug = judul_artikel.lower().replace(" ", "-").strip("!", "?", "_")
print(slug)