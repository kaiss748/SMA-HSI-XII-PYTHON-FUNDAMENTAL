
print(f"="*50)
tengah = "SELAMAT DATANG DI PROGRAM KASIR CERDAS!".center(50, " ")
print(" " + tengah + " ")
print(f"="*50)

print(f"\n---Detail Barang 1---")
nama_barang = input("barang yang anda beli : ")
harga_barang = float(input("harga barang yang anda beli : "))
jumlah_barang = int(input("jumlah barang yang anda beli : "))

print(f"\n---Detail Barang 2---")
nama_barang_2 = input("barang yang anda beli : ")
harga_barang_2 = float(input("harga barang yang anda beli : "))
jumlah_barang_2 = int(input("jumlah barang yang anda beli : "))

total_1 = harga_barang * jumlah_barang
total_2 = harga_barang_2 * jumlah_barang_2
subtotal = total_1 + total_2

if subtotal > 150000:
    persen_diskon = 10
elif subtotal > 75000:
    persen_diskon = 5
else:
    persen_diskon = 0   

jumlah_diskon = subtotal * persen_diskon / 100
total_setelah_diskonn = subtotal - jumlah_diskon

ppn = total_setelah_diskonn * 0.11
total_final = total_setelah_diskonn + ppn


print(f"\nMenghitung total...\n")
print(f"="*50)
tengah = "STRUK PEMBELIAN ANDA".center(50, " ")
print(" " + tengah + " ")
print(f"="*50)

print("\nDetail Belanja:")
print(f"1. {nama_barang:15} ({harga_barang} x {jumlah_barang}) = Rp {total_1:,.2f} ")
print(f"2. {nama_barang_2:15} ({harga_barang_2} x {jumlah_barang_2}) = Rp {total_2:,.2f} ")
print("-"*50)
print(f"{'Subtotal':20} : Rp {subtotal:,.2f}")
print(f"{f'Diskon ({persen_diskon}%)':20} : - Rp {jumlah_diskon:,.2f}")
print(f"{f'PPN (11%)':20} : + Rp {ppn:,.2f}")
print("-"*50)
print(f"Total yang harus dibayar : Rp {total_final:,.2f}")

print("="*50)
uang_bayar = float(input("Masukkan nominal yang dibayarkan (Rp): "))
kembalian = uang_bayar - total_final
print(f"{'Uang diterima':20} : Rp{uang_bayar:,.2f}")
print(f"{'Kembalian':20} : Rp{kembalian:,.2f}")

print(f"="*50)
tengah = "TERIMA KASIH TELAH BERBELANJA!".center(50, " ")
print(" " + tengah + " ")
print(f"="*50)




