"""
Latihan 23: Segitiga Huruf Alfabet
Buat program yang mencetak segitiga yang berisi urutan huruf alfabet.
Input: N = 5
Output yang diharapkan:
A
AB
ABC
ABCD
ABCDE
Petunjuk: Kamu perlu mengonversi angka ke karakter. Gunakan fungsi chr() dan ord(). ord('A')
akan memberimu nilai ASCII untuk 'A'. Kamu bisa menambahkan nilai loop j ke ord('A') lalu
mengubahnya kembali ke karakter dengan chr().
"""

N = int(input("Beri nilai N: "))
for i in range(1, N+1):
    for j in range(i):
        huruf = chr(ord('A')+j)
        print(f"{huruf}", end="")
    print()

