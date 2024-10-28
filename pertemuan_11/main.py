# Penjelasan tentang fungsi dan methods perbedaanya:
# - Fungsi adalah blok kode yang dapat dipanggil dengan memberikan 
# input tertentu dan mengembalikan output tertentu.
# - Method adalah fungsi yang terasosiasi dengan sebuah objek 
# dan dapat mengakses data yang terkait dengan objek tersebut.


def CetakNama(nama):
    print(nama)

CetakNama("John")


class Human:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        # print("hello my name is "+self.name+"i am from "
        #       +self.address+", i am "+str(self.age)+" years old")
            print(f"hello, my name is {self.name} and i am from "
            f"{self.address}, i am {str(self.age)} years old")
                
human_pertama = Human("john", 20,"jalan garuda")
human_pertama.greeting()

# tugas
# buatlah class bernama house yang memiliki property (type,height,width,material,..)minimal 6 attribut
# buatlah method untuk menampilan kalimat "rumah dengan tipe.... dan lebar x tingginya" (showDetail)
# buatlah method untuk menampilan kalimat "rumah dengan tipe.... yang berbahan material ......" (showMaterial)
# nama methodnya bebas


