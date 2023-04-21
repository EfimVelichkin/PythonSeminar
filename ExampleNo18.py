Num = int(input('Введите кол-во чисел: '))
Arr = [int(input()) for i in range (Num)]
x = int(input('Введите число с которым будем сравнивать: '))

mindiff = float('inf')
closest = None

for i in range(Num):
    diff = abs(Arr[i] - x)
    if diff < mindiff:
        mindiff = diff
        closest = Arr[i]

print(closest, 'Ближайшее число')