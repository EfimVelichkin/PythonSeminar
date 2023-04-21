import random
N = int(input('Введите кол-во чисел: '))
X = int(input('Какое число вы ищете? '))
j = int(0)
i = int(0)
Num = []
for i in range (N):
    Num.append(random.randint(1,N))
    if (X == Num[i]):
        j += 1
    i += 1
print(Num," ", j, ' - кол-во искомых чисел в списке')
