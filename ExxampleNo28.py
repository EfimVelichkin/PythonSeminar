a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a+1, b-1)

print(f"Сумма чисел {a} и {b} равна {sum(a, b)}")