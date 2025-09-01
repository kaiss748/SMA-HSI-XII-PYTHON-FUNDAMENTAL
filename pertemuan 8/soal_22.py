"""
Latihan 22: Diamond Bintang
Buat program yang mencetak bentuk berlian (diamond) setinggi N (N harus ganjil).
Input: N = 5
Output yang diharapkan:
  *
 ***
*****
 ***
  *
Petunjuk: Pecah masalah ini menjadi dua bagian. Buat satu for loop besar untuk mencetak piramida
bagian atas, lalu buat for loop besar kedua untuk mencetak piramida terbalik di bagian bawah.
"""

N = int(input("Beri nilai N: "))
for i in range(N // 2 + 1):
    spasi = (N // 2) - i
    bintang = 2 * i + 1
    print(" "* spasi, "*"*bintang)

for i in range(N // 2 -1, -1, -1):
    spasi = (N // 2) - i
    bintang = 2 * i + 1
    print(" "* spasi, "*"*bintang)

"""
range(N // 2 + 1) -> N nya dipecah menjadi 2...
N = 5...
5 // 2 = 2... kemudian di tambah 1 = 3

spasi = (N // 2) - i
5 // 2 = 2... kemudian di kurang i
karena range(i) mulai dari 0:
maka baris pertama -= 0
maka baris pertama -= 1
maka baris pertama -= 2

bintang = 2 * i + 1
karena range(i) mulai dari 0:
maka i pertama = 2*0 lalu di tambah 1 = 1
maka i kedua = 2*1 lalu di tambah 1 = 3
maka i ketiga = 2*2 lalu di tambah 1 = 5

for i in range(N // 2 -1, -1, -1)
start, stop, step
start dari N // 2 -1 yang berarti 2 - 1 = 1
stop sampai -1 supaya index ke=0 masi masuk
step -1 yang artinya perhitungan mundur
"""
   
