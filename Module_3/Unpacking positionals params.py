"""
Задача "Распаковка":
1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию
(например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
3.Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
"""


def print_params(a=1, b='строка', c=True):
    return print(a, b, c)


print_params()
print_params(5, "HP")
print_params(3, c="Wise")

print_params(b = 25)            # Обе строчки работают
print_params(c = [1,2,3])       # корректно

values_list = [39, 'рыба', [55, 42]]
values_dict = {'a': 100, 'b': "Cat", 'c': [*range(6)]}  # Название ключа должно совпадать с названием парамера в
print_params(**values_dict)                             # объявлении функции
print_params(*values_list)

values_list_2 = ['and', False]
print_params(*values_list_2, 42)
"""
Работает, но всё подставляется по порядку - сначала список на первые 2 слота, затем 42 на третий слот
(подсказка IDE неверная), но так делать не рекомендуется
"""