"""
Latihan 5: URL Slug Generator
Di dunia web, "slug" adalah versi URL-friendly dari sebuah judul artikel. Buat program yang mengubah judul
artikel menjadi slug. Aturannya:
    1. Ubah semua huruf menjadi kecil.
    2. Ganti semua spasi dengan tanda hubung (-).
    3. (Bonus) Hapus semua karakter selain huruf, angka, dan tanda hubung.
Contoh: judul = "10 Tips Jitu Belajar Python!"
Output yang diharapkan: "10-tips-jitu-belajar-python"
"""

judul_artikel = input("Masukan judul artikel : ")
slug = judul_artikel.lower().replace(" ", "-").strip("!", "?", "_")
print(slug)