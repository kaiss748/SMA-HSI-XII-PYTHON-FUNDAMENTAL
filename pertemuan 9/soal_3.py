#3.
kata = input("masukkan kata : ")
kata_terbalik = kata[::-1]
print(f"'{kata}' dibalik menjadi '{kata_terbalik}'")

if kata == kata_terbalik:
    print("kata tersebut adalah palindrom!")
else:
    print("kata tersebut bukan palindrom!")