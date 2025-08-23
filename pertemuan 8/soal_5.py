#5.
n = int(input("Masukka bilangan bulat positif : "))
hasil_faktoral = 1 #sbg akumulator perkalian
for i in range(1, n + 1): #menghitung 1 sampai nilai n
    hasil_faktoral *= i

print(f"Faktorial dari {n} adalah {hasil_faktoral}")
