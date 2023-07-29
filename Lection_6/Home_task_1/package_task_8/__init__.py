'''
Задача 8
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
'''

from Lection_6.Home_task_1.package_task_8.module_task_2_task_3 import func
from Lection_6.Home_task_1.package_task_8.module_task_4_task_5_task_6 import show_rezult, puzzle_solver, puzzle_solut
from Lection_6.Home_task_1.package_task_8.module_task_7 import calend, is_leap_year

__all__ = ["func", "show_rezult", "puzzle_solver", "puzzle_solut", "calend", "is_leap_year"]