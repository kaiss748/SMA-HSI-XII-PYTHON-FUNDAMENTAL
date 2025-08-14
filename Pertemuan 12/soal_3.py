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