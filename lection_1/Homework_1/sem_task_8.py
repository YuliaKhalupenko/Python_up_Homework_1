# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки?
#    *
#    ***
#   *****
#  *******
# *********


rows = int(input("Сколько рядов у ёлки? "))
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)