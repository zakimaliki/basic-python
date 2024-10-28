def konversi(num):
    if num > 80 and num <= 100 :
        print("Nilai : A")
    elif num > 60 and num <= 80:
        print("Nilai : B")
    elif num > 40 and num <= 60 :
        print("Nilai : C")
    elif num > 20 and num <= 40:
        print("Nilai : D")
    elif num <= 20 :
        print("Nilai : E")
    else :
        print("Nilai salah!")
