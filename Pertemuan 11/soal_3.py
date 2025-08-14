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