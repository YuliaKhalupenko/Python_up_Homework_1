#Создайте функцию генератор чисел Фибоначчи

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

fib_num = int(input("Сколько чисел Фибаначчи вывести: "))
print(*fibonacci(fib_num))
