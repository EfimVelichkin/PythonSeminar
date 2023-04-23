from random import randint

Bushes = int(input('Введите кол-во кустов: '))
Module = int(3)
Arr = []

for i  in range (Bushes):
    Arr.append(randint(30,200))
print(Arr,' Все кусты')
Arr.sort()
print(Arr[-Module:],' Самые большие кусты')
print(sum(Arr[-Module:]))