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



    
