# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import *

numerator1 = Fraction(input("Введите числитель первой дроби: "))
denominator1 = Fraction(input("Введите знаменатель первой дроби: "))
numerator2 = Fraction(input("Введите числитель второй дроби: "))
denominator2 = Fraction(input("Введите знаменатель второй дроби: "))

f1 = Fraction(numerator1, denominator1)
f2 = Fraction(numerator2, denominator2)
print(f1 + f2, f1 * f2)

LCD = denominator1 * denominator2

print(f"Сумма дробей = {numerator1 * denominator2 + numerator2 * denominator1}/{LCD}")
print(f"Произведение дробей = {numerator1 * numerator2}/{denominator1 * denominator2}")
