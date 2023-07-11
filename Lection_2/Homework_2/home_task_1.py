# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def decimal_to_hex(number: int) -> str:
    # Проверка на ноль
    if number == 0:
        return '0'

    hexadecimal: str = ''
    # Преобразование числа в шестнадцатеричное представление
    while number > 0:
        remainder: int = number % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('a') + remainder - 10) + hexadecimal
        number //= 16

    return hexadecimal


if __name__ == "__main__":
    number: int = int(input("Введите целое число: "))
    result: str = decimal_to_hex(number)
    print("Шестнадцатеричное представление числа:", result)
    print(f'Это шестнадцатеричное представление: {hex(number)[2:]}')