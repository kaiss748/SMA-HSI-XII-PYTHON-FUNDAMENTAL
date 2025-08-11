#1.
s = "Belajar Python itu Menyenangkan"
char_pertama = s[0]
print(f"Karakter pertama adalah: '{char_pertama}'")
char_terakhir = s[-1]
print(f"Karakter terakhir adalah: '{char_terakhir}'")  
char_spasi_pertama = s[7]
print(f"Karakter spasi pertama adalah: '{char_spasi_pertama}'")  


#2.
kata_pertama = s[8:14]
print(f"kata kedua adalah: '{kata_pertama}'")  
kata_kedua = s[19:]
print(f"kata keempat adalah: '{kata_kedua}'")  
kata_ketiga = s[:6+1]
print(f"kata pertama adalah: '{kata_ketiga}'")  


#3.
kata = input("masukkan kata : ")
kata_terbalik = kata[::-1]
print(f"'{kata}' dibalik menjadi '{kata_terbalik}'")

if kata == kata_terbalik:
    print("kata tersebut adalah palindrom!")
else:
    print("kata tersebut bukan palindrom!")

#4.
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
kode_rahasia = kalimat[::3]
print(f"kode rahasia adl '{kode_rahasia}'")

#5.
nama_salah = "dUDI sANTOSO"
nama_depan = "B" + nama_salah[1:4].lower() #memperbaiki, dUDI -> Budi
nama_belakang = "S" + nama_salah[6:].lower() #memperbaiki sANTOSO -> Santoso
nama_benar = nama_depan + " " + nama_belakang #menggabungkan nama yg telah diperbaiki
print(nama_depan)
print(nama_belakang)
print("Nama yang sudah diperbaiki:", nama_benar)

