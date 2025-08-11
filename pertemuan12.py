"""
Latihan 1: Membuat Log Sederhana
Buat program yang berfungsi sebagai buku catatan (log).
    1. Buka file bernama log_kegiatan.txt dalam mode append ('a').
    2. Minta pengguna memasukkan sebuah kegiatan yang baru saja mereka lakukan.
    3. Tulis input dari pengguna tersebut ke dalam file log_kegiatan.txt.
    4. Pastikan setiap entri log berada di baris baru.
Jalankan program ini beberapa kali untuk menambahkan beberapa entri log.
"""

file_kegiatan = "log_kegiatan.txt"
with open(file_kegiatan, 'a') as file:
    print(f"\nMenambah data kegiatan ke '{file_kegiatan}'...")
    print("ketik 'selesai' jika ingin menyimpan data")
    while True:
        kegiatan = input(f"Masukan data kegiatan: ")
        
        
        if kegiatan.lower() == "selesai":
            print(f"\nData berhasil disimpan:D")
            break
        
        file.write(kegiatan + "\n")


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


"""
Latihan 3: Hapus File dengan Aman
Buat program yang:
    1. Meminta pengguna memasukkan nama file yang ingin dihapus.
    2. Menggunakan os.path.exists() untuk mengecek apakah file tersebut benar-benar ada.
    3. Jika ada, program harus meminta konfirmasi sekali lagi (misal: "Anda yakin ingin menghapus [nama
file]? (y/n)").
    4. Jika pengguna mengetik 'y', gunakan os.remove() untuk menghapus file dan cetak pesan sukses.
    5. Jika pengguna mengetik selain 'y' atau jika file tidak ada, cetak pesan yang sesuai.
"""

import os
file_hapus = input("Masukan nama file yang ingin ko hapus: ")
if os.path.exists(file_hapus):
    confirm = input(f"Anda yakin ingin menghapus '{file_hapus}'? (y/n)").lower()
    
    
    if confirm == "y":
            os.remove(file_hapus)
            print("File berhasil dihapus:D")
    elif confirm == "n":
            print("lah? gak jadi dihapus_-")

    else:
        print("astaghfirullah, pilihannya cuma y/n aja masi salah_-")

else:
    print("filenya kaga ada boss_-")



    
