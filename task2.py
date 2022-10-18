# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


a = int(input('Введите длину списка: '))
my_list = [int(input ('Введите список:')) for _ in range (a)]
print(my_list)
new_list = []
for i in range(len(my_list) // 2 + len(my_list) % 2):
    new_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
print(new_list)