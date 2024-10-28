# aritmatika

# + , - , /, *, %

print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5%5)

# 
panjang = 20
lebar = 10

luasPersegi = panjang * lebar

print(luasPersegi)

# buat program untuk hitung luas lingkaran

# halfDia = int(input("masukan jar-jari : "))
halfDia = 10
pi = 3.14

luasLingkaran = pi * halfDia * halfDia

print(luasLingkaran)


# perbandingan

# >,<,==, >=,<=

print(5>10)
print(5<10)
print(5==10)
print(5>=10)
print(5<=10)

# logika

print(True and True) # keduanya bernilai True maka True
print(False or False) # Salah satu bernilai True maka True
print(not(False)) # Kebalikan

# syarat kenaikan itu rata UAS,UTS,UKK > 75 dan sudah membayar
# print("===========Aplikasi mulai===========")
# UAS = int(input("Masukan Nilai UAS :"))
# UTS = int(input("Masukan Nilai UTS :"))
# UKK = int(input("Masukan Nilai UKK :"))
# count = int(input("Masukan jumlah data :"))
# paid = True

# rataRata = (UAS+UTS+UKK)/count
# (uas+uts+ukk)/count

# if (rataRata>75 and paid):
#     print("Nilai rata-rata anda :"+ str(rataRata))
#     print("Selamat anda naik kelas!" )
# else:
#     print("Nilai rata-rata anda :"+ str(rataRata))
#     print("Mohon maaf anda belum naik kelas")


# Tugas buatlah aplikasi untuk menghitung rata rata murid jumlah di kelas A kelas B kelas C dan kelas D 
# Tugas buatlah aplikasi untuk mengkonversi dari cesius ke farenheit dan sebalikanya
print("============= Aplikasi konversi ============ ")
print("1 cesius ke farenheit ")
print("2 farenheit ke cesius ")
choice = int(input("Silahkan pilih : "))

if choice == 1:
    Celcius = float(input("Masukan nilai Celcius : "))
    Fahrenheit = ((9/5) * Celcius) + 32
    print(f"{Celcius} derajat Celsius sama dengan {Fahrenheit} derajat Fahrenheit")
elif choice == 2:
    Fahrenheit = float(input("Masukan nilai Fahrenheit : "))
    Celcius = (5/9) * (Fahrenheit - 32)
    print(f"{Fahrenheit} derajat Fahrenheit sama dengan {Celcius} derajat Celsius")
else :
    print("Inputan Salah!")
