Arr1 = int(input("Введите количество элементов первого множества: "))
Arr2 = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(Arr1):
    set1.add(int(input()))

print("Введите элементы второго множества:")
for i in range(Arr2):
    set2.add(int(input()))

commonelements = sorted(list(set1.intersection(set2)))

print("Элементы, которые встречаются в обоих множествах:", end=" ")
for element in commonelements:
    print(element, end=" ")