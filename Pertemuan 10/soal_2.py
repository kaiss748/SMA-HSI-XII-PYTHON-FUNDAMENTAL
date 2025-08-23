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
