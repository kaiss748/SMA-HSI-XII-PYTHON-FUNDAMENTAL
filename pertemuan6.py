#1.
def buat_email(nama_pengguna, domain="coding.com"):
    email = f"{nama_pengguna.lower()}@{domain.lower()}"
    return email

print(buat_email("Budi"))
print(buat_email("Ani", "belajar.id"))

#2.
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"mengirim {barang} ke {tujuan}")
    print(f"berat: {berat_kg} kg")
    print(f"asuransi: {asuransi}")
    print(f"express: {express}")

kirim_paket("Buku", "Bandung", "2", express=True)

#3.
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    nilai_rata_rata = total / jumlah_elemen if jumlah_elemen > 0 else 0
    return total, jumlah_elemen, nilai_rata_rata

angka = [10, 20, 30, 40, 50]
total, jumlah_elemen, nilai_rata_rata = analisis_daftar(angka)
print(f"total : {total}")
print(f"jumlah elemen : {jumlah_elemen}")
print(f"nilai_rata_rata : {nilai_rata_rata}")


#4.
def analisis_daftar(daftar_angka):
    """Menghitung jumlah total, jumlah elemen, nilai rata rata.

    fungsi ini menerima daftar angka/kumpulan angka, lalu mengembalikan nilai
    jumlah total, jumlah elemen, nilai rata rata.

    Args:
        daftar_angka (list of float or int) : kumpulan angka dalam bentuk list

    Returns:
         tuple: Tiga nilai berupa:
            - total (int or float): Jumlah semua angka dalam daftar.
            - jumlah_elemen (int): Banyaknya elemen dalam daftar.
            - rata_rata (float): Nilai rata-rata dari semua angka. 0 jika daftar kosong.
    """
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    nilai_rata_rata = total / jumlah_elemen if jumlah_elemen > 0 else 0
    return total, jumlah_elemen, nilai_rata_rata

angka = [10, 20, 30, 40, 50]
total, jumlah_elemen, nilai_rata_rata = analisis_daftar(angka)
print(f"total : {total}")
print(f"jumlah elemen : {jumlah_elemen}")
print(f"nilai_rata_rata : {nilai_rata_rata}")
# help(analisis_daftar)
print(analisis_daftar.__doc__)

#5.
luas_lingkaran_lambda = lambda radius : 3.14159 * (radius ** 2)
print("Hasil dari lambda:", luas_lingkaran_lambda(7))