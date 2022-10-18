# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


a = int(input('Введите длину списка: '))
my_list = [float(input ('Введите список:')) for _ in range (a)]
new_list = [float('0.' + str(i).split('.')[1]) for i in my_list if '.' in str(i)]
print(new_list)
print(max(new_list) - min(new_list))