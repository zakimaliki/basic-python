# lambda = fungsi tak bernama


x = lambda a: a * 10

print(x(10))



luasPersegiPanjang = lambda panjang,lebar : panjang * lebar

print(luasPersegiPanjang(10,10))


luasLingkaran = lambda jarijari : 3.14 * jarijari * jarijari

print(luasLingkaran(10))


luasSegitiga = lambda tinggi , lebar : 1/2 * tinggi * lebar

print(luasSegitiga(20,15))



# 1. buatlah lambda untuk menghitung rata nilai dari 5 mata kuliah
# 2. buatlah labda untuk menghitung nilai terkecil dari 5 mata kuliah
# 3. buatlah labda untuk menghitung nilai terbesar dari 5 mata kuliah

# frekuensi = float(input("masukan frekuensi:"))
# bhs_indo = float(input("masukan nilai bahasa indonesia:"))
# bhs_ing = float(input("masukan nilai bahasa inggris:"))
# math = float(input("masukan nilai matekatika:"))
# algoritma = float(input("masukan nilai algoritma:"))
# logika_informatika = float(input("masukan nilai logika informatika:"))

# # Definisi lambda function untuk menghitung rata-rata
# nilaiRataRata = lambda a, b, c, d, e, f: (a + b + c + d + e) / f

# Hitung dan tampilkan rata-rata
# rata_rata = nilaiRataRata(bhs_indo, bhs_ing, math, algoritma, logika_informatika, frekuensi)
# print(f"\nNilai rata-rata: {rata_rata}")

print("=================================================")
bhs_indo = float(input("masukan nilai bahasa indonesia:"))
bhs_ing = float(input("masukan nilai bahasa inggris:"))
math = float(input("masukan nilai matekatika:"))
algoritma = float(input("masukan nilai algoritma:"))
logika_informatika = float(input("masukan nilai logika informatika:"))

# Definisi lambda function untuk menghitung rata-rata
nilaiTerkecil = lambda a, b, c, d, e: min(a, b, c, d, e)

# Hitung dan tampilkan rata-rata
minimum = nilaiTerkecil(bhs_indo, bhs_ing, math, algoritma, logika_informatika)
print(f"\nNilai terkecil : {minimum}")






print("=================================================")
bhs_indo = float(input("masukan nilai bahasa indonesia:"))
bhs_ing = float(input("masukan nilai bahasa inggris:"))
math = float(input("masukan nilai matekatika:"))
algoritma = float(input("masukan nilai algoritma:"))
logika_informatika = float(input("masukan nilai logika informatika:"))

# Definisi lambda function untuk menghitung rata-rata
nilaiTerbesar = lambda a, b, c, d, e: max(a, b, c, d, e)

# Hitung dan tampilkan rata-rata
maksimum = nilaiTerbesar(bhs_indo, bhs_ing, math, algoritma, logika_informatika)
print(f"\nNilai terbesar : {maksimum}")


