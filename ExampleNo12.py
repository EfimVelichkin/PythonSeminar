import random

S = int(input('Назовите сумму двух загаданных чисел '))
P = int(input('Назовите произведение двух загаданных чисел '))

i = int(0)
while(i <= 0):
    X = random.randint(0,P)
    Y = random.randint(0,P)
    if(X+Y == S) and (X*Y == P):
        print(f'Загаданные числа {X} и {Y}')
        break