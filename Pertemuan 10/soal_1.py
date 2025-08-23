"""
Latihan 1: Standarisasi Judul
Buat program yang meminta pengguna memasukkan judul buku yang mungkin diketik dengan huruf
besar/kecil yang acak (misal: "aLaDiN dan LaMPu aJAib"). Programmu
"""

judul = input("Masukan judul : ")
final_judul = judul.strip().title()
print(final_judul)