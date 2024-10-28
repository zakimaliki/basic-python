# looping

print("1")
print("2")
print("3")
print("4")
print("5")

print('===================')

for i in range(5):
    print(i+1)

print('===================')


list = [1,2,3,4,5,6,7,8,9,10]

for i in  list:
    print(i)

print('===================')

count = 0

while count < 5:
    print(count+1)
    count+=1

print('===================')

# Menampilkan bilangan genap dari deret 1-100
for i in range(101):
    if(i % 2 == 0):
        print(f"{i} bilangan genap")
    else:
        print(f"{i} bilangan ganjil")

# no 1 tampilkan deret angka bilangan prima dari 0 - 100 menggunhkan for
# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# no 2 tampilkan deret angka bilangan prima dari 0 - 100 menggunhkan while
# num = 2
# while num <= 100:
#     is_prime = True
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num)
#     num += 1
