"""
Latihan 25: Piramida Angka Palindromik
Buat program yang mencetak piramida angka yang simetris.
Input: N = 5
Output yang diharapkan:
    1
   121
  12321
 1234321
123454321
Petunjuk: Ini adalah yang paling menantang. Setiap baris terdiri dari tiga bagian: spasi, urutan angka
naik, dan urutan angka turun. Kamu mungkin perlu tiga loop terpisah di dalam loop baris utama: satu
untuk spasi, satu untuk angka naik, dan satu untuk angka turun.
"""

N = int(input("Beri nilai N: "))
for i in range(1, N+1):
    for s in range(N - i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()


"""
ditulis j biar angka nya bukan 1, 22, 333...
tapi biar ngulang lagi dari awal sampe ke i

bgtu pula k
"""
