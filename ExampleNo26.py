def recursuion(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * recursuion(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

print(f"{a} в степени {b} равно {recursuion(a, b)}")