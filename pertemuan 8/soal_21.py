"""
Latihan 21: Persegi Bolong (Hollow Square)
Buat program yang mencetak bingkai persegi berukuran N x N.
Input: N = 5
Output yang diharapkan:
*****
*   *
*   *
*   *
*****
Petunjuk: Di dalam nested loop, gunakan if-else. Cetak bintang (*) hanya jika kamu berada di
baris pertama (i == 0), baris terakhir (i == N-1), kolom pertama (j == 0), atau kolom terakhir (j
== N-1). Jika tidak, cetak spasi.
"""
N = int(input("Beri nilai N: "))
for i in range(N):
    for j in range(N):
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()