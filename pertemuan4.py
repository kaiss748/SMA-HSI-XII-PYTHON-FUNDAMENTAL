# 1. 

jam_kerja = int(input("berapa jam anda kerja? "))
jam_normal = 40
tarif = 10

if jam_kerja <= jam_normal:
    total_upah = jam_kerja*tarif
else:
    lembur = jam_kerja - jam_normal
    total_upah = (jam_normal*tarif) + (lembur*tarif*1.5)

print("pay : ", total_upah)
  

# 2.

try:
    jam_kerja = float(input("berapa jam anda kerja? "))
    tarif_kerja = float(input("berapa tarif perjam? "))
    jam_normal = 40

    if jam_kerja <= jam_normal:
        total_upah = jam_kerja*tarif
    else:
        lembur = jam_kerja - jam_normal
        total_upah = (jam_normal*tarif) + (lembur*tarif*1.5)
        
    print("pay : ", total_upah)

except:
    print("Error, please enter numeric input")
finally:
    print("terima kasih telah menggunakan layanan ini :D")


#>= 0.9 -> A
#>= 0.8 -> B
#>= 0.7 -> C
#>= 0.6 -> D
#< 0.6 -> F






# 3.
score_str =input("masukkan skor ujian anda (0.0 - 1.0)")
try:
    score = float(score_str)

    if score < 0.0 or score > 1.0 :
        print("Error, skor harus diantara 0.0 - 1.0")
    else:
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"
        print("grade kamu adalah ", grade)

except:
    print("skor harus berupa angka")
finally:
    print("thank you for using this program :D")


# 4.
tinggi_cm = 150
usia = 12
didampingi_ortu = True

if tinggi_cm >= 150 and (usia >= 12 or didampingi_ortu):
    print("boleh masuk")
else:
    print("tidak layak masuk")
