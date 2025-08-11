def tampilan_header():
    print("="*50)
    tampilan_header = "SELAMAT DATANG DI TOKO MASA DEPAN!".center(50, " ")
    print(" " + tampilan_header + " ")
    print("="*50)
    print(f"---Masukan Detail Barang---")
    print(f"(Ketik 'selesai' di nama barang untuk selesai)\n")

tampilan_header()

daftar_nama_barang = []
daftar_harga_barang = []
daftar_jumlah_barang = []

while True:
    #nantinya diisi oleh nama barang, harga, jumlah
    nama_barang = input("Nama Barang : ")
    if nama_barang.lower() == 'selesai':
        print("\nMenghitung total belanja anda...\n")
        break

    try:
        harga_barang = int(input("Harga Barang : "))
        jumlah_barang = int(input("Jumlah Barang : "))
        print(f"---Barang berhasil ditambahkan!---\n")


        daftar_nama_barang.append(nama_barang)
        daftar_harga_barang.append(harga_barang)
        daftar_jumlah_barang.append(jumlah_barang)

    except ValueError:
        print("Input harga dan jumlah harus berupa angka! Silakan ulangi.\n")
        continue  # kembali ke atas loop untuk input ulang
    

def hitung_subtotal(daftar_harga, daftar_jumlah):
    subtotal = 0
    for i in range(len(daftar_harga)):
        subtotal += daftar_harga[i] * daftar_jumlah[i]
    return subtotal

def hitung_diskon(subtotal):
    if subtotal > 150000:
        persen_diskon = 15
    elif subtotal > 75000:
        persen_diskon = 7
    else:
        persen_diskon = 0   

    total_diskon = subtotal * persen_diskon / 100
    total_bayar = subtotal - total_diskon
    return persen_diskon, total_diskon, total_bayar

def tampilan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal,
total_diskon, persen_diskon, total_bayar):
    print(f"="*50)
    tengah = "STRUK PEMBELIAN ANDA".center(50, " ")
    print(" " + tengah + " ")
    print(f"="*50)
    print("Detail belanja : \n")

    for i in range(len(daftar_nama_barang)):
        total_item = daftar_harga_barang[i] * daftar_jumlah_barang[i]
        print(f"{i+1}. {daftar_nama_barang[i]:10} (Rp {daftar_harga_barang[i]:,.2f} x {daftar_jumlah_barang[i]}) = Rp {total_item:,.2f}")

    print("-"*50)
    print(f"{'Subtotal':20} : Rp {subtotal:,.2f}")
    print(f"{f'Diskon ({persen_diskon}%)':20} : - Rp {total_diskon:,.2f}")
    print("-"*50)
    print(f"Total yang harus dibayar : Rp {total_bayar:,.2f}")
    print(f"="*50)
    print(f"TERIMAKASIH TELAH BERBELANJA!".center(50))
    print(f"="*50)

subtotal = hitung_subtotal(daftar_harga_barang, daftar_jumlah_barang)
persen_diskon, total_diskon, total_bayar = hitung_diskon(subtotal)
# total_bayar = subtotal - total_diskon

tampilan_struk(daftar_nama_barang, daftar_harga_barang, daftar_jumlah_barang, subtotal,
total_diskon, persen_diskon, total_bayar)