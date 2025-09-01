"""
Latihan 16: Persegi Bintang Solid
Buat program yang mencetak persegi solid yang terdiri dari bintang (*) berukuran N x N.
Input: N = 5
Output yang diharapkan:
*****
*****
*****
*****
Petunjuk: Kamu akan butuh dua for loop yang bersarang (nested). Loop luar untuk baris, loop
dalam untuk kolom.
"""

N = int(input("Beri nilai N: "))
for i in range(1, N+1):
    for j in range(N):
        print(f"*", end=" ")
    print()