def circle():
    R = int(input("Radius engiziniz: "))
    print(3.14*(R**2))

def Square():
    n = int(input("Qabirga uzyndygyn engiziniz: "))
    print(n*n)

def rectangle():
    width = int(input("Uzyndygyn engiziniz: "))
    height = int(input("Biyktikti engiziniz: "))

    print(width*height)

print("Пішінді таңдаңыз:\n1 Шаршы\n2. Тіктөртбұрыш\n3. Шеңбер")
n = int(input("Таңдауыңызды енгізіңіз (1/2/3): "))
if n == 1:
    Square()
elif n == 2:
    rectangle()
else:
    circle()