# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

A_SIDE = int(input('Введите сторону А: '))
B_SIDE = int(input('Введите сторону В: '))
C_SIDE = int(input('Введите сторону С: '))

result = None

if A_SIDE > B_SIDE + C_SIDE or B_SIDE > A_SIDE + C_SIDE or C_SIDE > A_SIDE + B_SIDE or \
    A_SIDE == B_SIDE == C_SIDE == 0:
    result = 'Такого треугольника не существует'
elif A_SIDE == B_SIDE == C_SIDE:
    result = 'Это равносторонний треугольник'
elif A_SIDE != B_SIDE != C_SIDE != A_SIDE:
    result = 'Это разносторонний треугольник'
else:
    result = 'Это равнобедренный треугольник'
print(result)