import random

N = int(input('Введите кол-во монеток: '))
i = int(1)
Reshka = int(0)
Eagle = int(0)

while(i <= N):
    Coin = random.randint(0, 1)
    i += 1
    if(Coin == 1):
        Reshka += 1
    else:
        Eagle += 1
if(Reshka > Eagle):
    Num = N - Reshka
    print(f'Надо перевернуть {Num} монеток орлами вверх')
else:
    Num = N - Eagle
    print(f'Надо перевернуть {Num} монеток решками вверх')
    
