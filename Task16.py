# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

N = int(input("Введите количество элементов массива: "))
A = list(map(int, input("Введите по одному числу через пробел: ").split()))
X = int(input("Введите число: "))
if X in A:
    print("Введенное Вами число встречается " + str(A.count(X)) + (" раз(а)"))
else:
    print("Введенного Вами числа здесь нет!")


