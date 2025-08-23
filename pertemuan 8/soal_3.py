#3.
total = 0
for angka in range(1, 51):
    if angka % 3 == 0 and angka % 5 == 0:
        total += 1 #menghitung berapa kali pembagian diatas terjadi
print(f"jumlah angka yang habis dibagi 3 dan 5 -> {total}")