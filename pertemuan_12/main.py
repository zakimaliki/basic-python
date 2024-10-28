# inheritance = pewarisan sifat


# class parent
# class Human:
#     def __init__(self,name,age):
#         self.name = name;
#         self.age = age;

# # class child
# class Student(Human):
#     pass

# pass memungkinkan class child mewarisi semua sifat class parent tanpa dekalrasi

# student_first = Student("john", 19)
# print("Property of Student:")
# print(student_first.name)
# print(student_first.age)









# class parent
class Human:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

# class child
class Student(Human):
    def __init__(self,name,age):
        # Human.__init__(self,name,age)
        super().__init__(name,age)

# super memungkinkan class child mewarisi semua sifat class parent dengan deklarasi


student_first = Student("john", 19)
print("Property of Student:")
print(student_first.name)
print(student_first.age)






# class parent
class Human:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;

# class child
class Student(Human):
    def __init__(self,name,age,nim):
        # Human.__init__(self,name,age)
        super().__init__(name,age)
        self.nim = nim

    def Greating(self):
        print("Hello, I am a student with NIM " + self.nim)

        
#super memungkinkan class child mewarisi semua sifat class parent dengan deklarasi


student_first = Student("john", 19, "121345566")
print("Property of Student:")
print(student_first.name)
print(student_first.age)
print(student_first.nim)
student_first.Greating()




# latihan 


class Mamal:
    def __init__(self, breathing_type, produces_milk):
        self.breathing_type = breathing_type
        self.produces_milk = produces_milk


# child class
class Cow(Mamal):
    pass


class sheep(Mamal):
    def __init__(self, breathing_type, produces_milk,type,legs):

