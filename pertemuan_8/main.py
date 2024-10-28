# fungsi sederhana
def greeting():
    print("Hello World!")

greeting()

# fungsi yang ada parameter

def greeting(nama):
    print(f"Hello {nama}!")

nama = "stephen"
greeting(nama)

# fungsi yang ada return

def penjumlahan(x,y):
    return x + y

hasil = penjumlahan(10,5)
print(hasil)

def penjumlahan(x,y):
    print( x + y)

penjumlahan(10,5)

# buatlah fungsi pengurang , perkalian, pembagian

def luasPersegi(panjang,lebar):
    print(panjang*lebar)

luasPersegi(100,200)

# no 1 . buatlah fungsi menghitung luas segitiga
# no 2 . buatlah fungsi untuk menghitung luas lingkaran
# no 3 . buatlah fungsi untuk menampilkan bilangan genap 1-10