def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Часть 1: Функция с параметрами по умолчанию
print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(5, b='новая строка')

# Часть 2: Распаковка параметров
values_list = [42, 'текст', False]
values_dict = {'a': 99, 'b': 'словарь', 'c': [True, False]}
print_params(*values_list)
print_params(**values_dict)

# Часть 3: Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
