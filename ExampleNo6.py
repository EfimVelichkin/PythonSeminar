Ticket = int(input('Введите билет: '))
Tick = Ticket
Num1 = Tick % 10
Tick = Tick // 10
Num2 = Tick % 10
Tick = Tick // 10
Num3 = Tick % 10
Tick = Tick // 10
Num4 = Tick % 10
Tick = Tick // 10
Num5 = Tick % 10
Tick = Tick // 10
Num6 = Tick % 10
print(Num1, Num2, Num3, Num4, Num5, Num6)
Sum1 = Num1+Num2+Num3
Sum2 = Num4+Num5+Num6
if(Sum1 == Sum2):
    print(Ticket,' Счастливый билет')
else:
    print(Ticket,' Не счастливый билет')