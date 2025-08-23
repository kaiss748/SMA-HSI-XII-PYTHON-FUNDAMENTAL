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