#1.

for i in range(0, 70, 7):
    print(i)

#2.
kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print(f"kalimat_terbalik : {kalimat_terbalik}")

#3.
total = 0
for angka in range(1, 51):
    if angka % 3 == 0 and angka % 5 == 0:
        total += 1 #menghitung berapa kali pembagian diatas terjadi
print(f"jumlah angka yang habis dibagi 3 dan 5 -> {total}")

#4.
for i in range(5, 0, -1):
    for j in range(i):
        print(f"*", end="") #mencetak tanpa harus pindah baris
    print() #untuk pindah baris setelah 1 baris bintang selesai

#5.
n = int(input("Masukka bilangan bulat positif : "))
hasil_faktoral = 1 #sbg akumulator perkalian
for i in range(1, n + 1): #menghitung 1 sampai nilai n
    hasil_faktoral *= i

print(f"Faktorial dari {n} adalah {hasil_faktoral}")
