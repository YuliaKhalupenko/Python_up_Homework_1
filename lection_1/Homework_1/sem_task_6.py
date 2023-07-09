#Напишите программу, которая запрашивает год и проверяет его на високосность.
#Распишите все возможные проверки в цепочке elif
#Откажитесь от магических чисел
#Обязательно учтите год ввода Григорианского календаря
#В коде должны быть один input и один print

START_YEAR = 1582
CHECK_NORMAL_1 = 4
CHECK_NORMAL_2 = 100
CHECK_NORMAL_3 = 400
result = ''
year = int(input('Введите год в формате уууу: '))
if year < START_YEAR:
    result = 'Вы ввели не верную дату'
elif year % CHECK_NORMAL_1:
    result = 'ваш год не високосный'
elif not year % CHECK_NORMAL_2:
    if not year % CHECK_NORMAL_3:
        result = 'ваш год високосный'
    else:
        result = 'ваш год не високосный'
else:
    result = 'ваш год високосный'
print(result)
