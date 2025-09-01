"""
Latihan 19: Piramida Bintang
Buat program yang mencetak piramida (segitiga sama kaki) setinggi N.
Input: N = 5
Output yang diharapkan:
    *
   ***
  *****
 *******
*********
Petunjuk: Ini adalah tantangan pertama yang membutuhkan logika spasi. Di setiap baris, kamu perlu
mencetak sejumlah spasi, diikuti oleh sejumlah bintang. Coba temukan rumus untuk jumlah spasi dan
jumlah bintang untuk setiap baris i. Jumlah spasi biasanya N - 1 - i dan jumlah bintang 2 * i + 1
"""

N = int(input("Beri nilai N: "))
for i in range(N):
    for s in range(N - 1 - i):
        print(f" ", end="")
    for j in range(2 * i + 1):
        print(f"*", end="")
    print()