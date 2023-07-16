#Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def absolute_path(path: str) -> tuple:
    file_name = path.split("/")[-1]
    file_extension = file_name.split('.')[1]
    result = path, file_name, file_extension
    return result


path = 'C:/Users/Rosya/Desktop/учеба/python/Homework/python_up/Lection_5/Homework_5/file.txt'
print(absolute_path(path))
