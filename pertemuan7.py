#1.
angka = 10

while angka > 0:
    angka -= 1
    print(angka)

print("Blastoff!")

#2.
angka_rahasia = 7

while True:
    try:
        tebakan = int(input("manakah angka yang benar (0-20) : "))
        if tebakan < 0 or tebakan > 20:
            print("kan perintahnya antara (0-20) bijak_-")

        if tebakan == angka_rahasia:
            print("welcome to San Vaganza")
            break
        else :
            print("salah!, pergilah wahai anomali!!!")
            print("jawab yang bener aneh_-")
    except:
        print("kan perintahnya antara (0-20) pandai_-")
print("thankyou for using this program :D")


#3.
final = 0
count = 0

while True:
    data = input("masukkan angka : ")
    if data == "done":
        break

    try :
        angka = float(data)
        final += angka
        count += 1
    except :
        print("input tidak valid")
        continue

if count > 0:
    rata_rata = final / count
    print(f"jumlah angka : {count}")
    print(f"total : {final}")
    print(f"rata rata : {rata_rata}")
else:
    print("tidak ada angka yang dimasukkan.")






