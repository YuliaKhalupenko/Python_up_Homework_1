"""
Задача 4
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""

from my_pacage_task8.module_task4_task5_task6 import puzzle


if __name__ == '__main__':
    print(puzzle("Зимой и летом одним цветом", ['ель', 'елка', 'доллар'], 3))


'''
Задача 5
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

'''
from my_pacage_task8.module_task4_task5_task6 import puzzle_solut


if __name__ == '__main__':
    print(puzzle_solut())

'''
Задача 6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и
число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

'''
from my_pacage_task8.module_task4_task5_task6 import puzzle_solver, show_rezult
import random

if __name__ == '__main__':
    puzzle_solver('Зимой и летом одним цветом', random.randint(3,6))
    puzzle_solver('Висит груша - нельзя скушать', random.randint(3,6))
    show_rezult()