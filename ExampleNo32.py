min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))
array = input("Введите массив через пробел: ").split()

result = []

for i in range(len(array)):
    if int(array[i]) >= min_value and int(array[i]) <= max_value:
        result.append(i)

print("Исходный массив:", array)
print("Индексы элементов, значения которых принадлежат заданному диапазону:", result)