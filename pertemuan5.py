#1.
def salam_pembuka():
    print("="*30)
    print("Selamat Datang di Program Saya!")
    print("="*30)

salam_pembuka()

#2.
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")

info_cuaca("solo", "hujan badai angin ribut")

#3.
def kubik(angka):
    return angka ** 3

hasil_kubik = kubik(4)

print(hasil_kubik)

#4.
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal*(persen_diskon/100)
    harga_akhir = harga_awal - jumlah_diskon
    return harga_akhir

harga_input = float(input("masukkan harga :"))
diskon_input = float(input("masukkan presentase diskon (%) :"))

hitung_akhir = hitung_diskon(harga_input, diskon_input)
print(f"total biaya yang harus kmu bayar : Rp{hitung_akhir:,.2f}")

#5. 
def fahrenheit_ke_celcius(temp_f):
    return (temp_f - 32) * 5/9.

celcius = fahrenheit_ke_celcius(98.6)
print(f"hasil konversi : {celcius:.2f}")

