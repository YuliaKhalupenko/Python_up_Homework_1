'''
функция из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''


from pathlib import Path
import os


def create_dir(name_dir: str):
    #
    name = Path(
        Path.cwd() / name_dir)  # C:\Users\Алексей\Desktop\GreekBrains\СЕМИНАРЫ\Python_advanced\pythonProject\new
    if not name.exists():  # проверка на наличие директория
        name.mkdir()  # создает директорий с именем name_dir в текущем директории
    # os.chdir(name)  # переходим в созданный каталог сделав его текущим