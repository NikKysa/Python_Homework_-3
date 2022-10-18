# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.

# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


a = int(input('Введите число для ряда Фибоначчи: '))
fibonaccilist = [0]*(a*2+1)
fibonaccilist[a] = 0
fibonaccilist[a+1] = 1

for i in range(a+2, len(fibonaccilist)):
    fibonaccilist[i] = fibonaccilist[i-2] + fibonaccilist[i - 1]

for i in range(a, -1, -1):
    fibonaccilist[i] = fibonaccilist[i+2] - fibonaccilist[i+1]

print(fibonaccilist)