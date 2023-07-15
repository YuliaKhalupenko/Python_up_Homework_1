#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.


from collections import Counter
print('-'*20, 'Test 2', '-'*20)
list_test = [1,1,2,3,3,4,5,6,6,3,7,8,8,9]
list_dup_1 = set([x for x in list_test if list_test.count(x) > 1])
list_dup_2 = [x for x,k in Counter(list_test).items() if k > 1]
print(list_test)
print(list(list_dup_1))
print(list_dup_2)
