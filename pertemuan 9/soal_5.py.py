 #5.
nama_salah = "dUDI sANTOSO"
nama_depan = "B" + nama_salah[1:4].lower() #memperbaiki, dUDI -> Budi
nama_belakang = "S" + nama_salah[6:].lower() #memperbaiki sANTOSO -> Santoso
nama_benar = nama_depan + " " + nama_belakang #menggabungkan nama yg telah diperbaiki
print(nama_depan)
print(nama_belakang)
print("Nama yang sudah diperbaiki:", nama_benar)

