import copy

#Задача 1. Challenge-2
print("Задача 1. Challenge-2")
#Что нужно сделать
#Вдохновившись мотивацией Антона, ваш друг тоже решил поставить перед собой задачу, но не напрямую связанную с математикой,
#а именно: написать функцию, которая выводит все числа от 1 до num без использования циклов.
#Помогите другу реализовать такую функцию.

num = int(input("Введите num: "))
print()
start = 1
def print_numbers(num, start):
	print(start)
	print()
	start += 1
	if start == num:
		print(start)
		return
	else:
		print_numbers(num, start)
print_numbers(num, start)
print()

#Задача 2. Поиск элемента — 2
print("Задача 2. Поиск элемента — 2")
#Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень,
#до которого будет просматриваться структура. 
#
#Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран.
#По умолчанию уровень не задан. В качестве примера можно использовать такой словарь:

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key, max_depth=None, current_depth=0):
    if max_depth is not None and current_depth >= max_depth:
        return None
    
    if key in struct:
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, current_depth + 1)
            if result is not None:
                return result
    return None

user_key = input("Введите искомый ключ: ")

while True:
    use_max_deep = input("Хотите ввести максимальную глубину? Y/N: ").lower()
    if use_max_deep in ("y", "n"):
        break
    print("Некорректный ввод. Введите Y или N.")

if use_max_deep == "y":
    max_deep = int(input("Введите максимальную глубину: "))
else:
    max_deep = None

value = find_key(site, user_key, max_deep)

print(f"Значение ключа: {value}")
print()

#Задача 3. Глубокое копирование
print("Задача 3. Глубокое копирование")
print()
#Что нужно сделать
#Вы сделали для заказчика структуру сайта по продаже телефонов:

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

#Заказчик рассказал своим коллегам на рынке, и они захотели такой же сайт для своих товаров. Вы посчитали, что это лёгкая задача, и быстро принялись за работу. 
#
#Напишите программу, которая запрашивает у клиента количество сайтов, затем названия продуктов, а после каждого запроса выводит на экран активные сайты. 
#
#Условия: 
#
#учтите, что функция должна уметь работать с разными сайтами (иначе вам придётся переделывать программу под каждого заказчика заново);
#вы должны получить список, хранящий сайты для разных продуктов (а значит, для каждого продукта нужно будет первым делом выполнить глубокое копирование сайта).

def deep_copy(obj):
    if isinstance(obj, (int, float, bool, str)):
        return obj
    elif isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}
    else:
        return copy.deepcopy(obj)
    
def create_sites(num):
	sites = []
	sites.append(site)
	for i in range(num):
		product_name = input(f"Введите название продукта {i + 1}: ")
		new_site = deep_copy(site)
		new_site['html']['head']['title'] = f"Куплю/продам {product_name} недорого"
		new_site['html']['body']['h2'] = f"У нас самая низкая цена на {product_name}"
		sites.append(new_site)
	return sites

num = int(input("Введите количество сайтов: "))
sites = create_sites(num)
print()
print("Активные сайты:")
for i, site in enumerate(sites, start=1):
	print(f"Сайт {i}:")
	print(site)
print()

#Задача 4. Продвинутая функция sum
print("Задача 4. Продвинутая функция sum")
print()
#Что нужно сделать
#Как вы знаете, в Python есть полезная функция sum, которая умеет находить сумму элементов списков.
#Иногда базовых возможностей функций не хватает для работы и приходится их усовершенствовать.
#
#Напишите свою функцию sum, которая должна быть более гибкой, чем стандартная. Она должна уметь складывать числа:
#
#из списка списков,
#набора параметров.
#Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

def my_sum(*args):
	total = 0
	for arg in args:
		if isinstance(arg, (int, float)):
			total += arg
		elif isinstance(arg, list):
			total += my_sum(*arg)
	return total
print(my_sum(1, 2, 3, 4, 5))
print(my_sum([[1, 2, [3]], [1], 3]))
print()

#Задача 5. Список списков — 2
print("Задача 5. Список списков — 2")

#Вы уже работали с многомерными списками и решали задачи, где с помощью list comprehensions «выпрямляли» многомерные списки в один.
#Это не получится, если списков неограниченное количество и у элементов разные уровни вложенности.
#Дан такой список:

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

#Напишите рекурсивную функцию, которая раскрывает все вложенные списки, то есть оставляет только внешний список.
#Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

#Функция должна получать список и возвращать его раскрытую версию (не нужно добавлять элементы в список, записанный в глобальную переменную, созданную снаружи функции).

def flatten_list(nice_list):
	result = []
	for item in nice_list:
		if isinstance(item, list):
			result.extend(flatten_list(item))
		else:
			result.append(item)
	return result

print(flatten_list(nice_list))
print()

#Задача 6. Быстрая сортировка
print("Задача 6. Быстрая сортировка")

#Реализуйте алгоритм быстрой сортировки (её называют сортировкой Хоара). 

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[-1]
		left = [x for x in arr if x < pivot]
		middle = [x for x in arr if x == pivot]
		right = [x for x in arr if x > pivot]
		return quicksort(left) + middle + quicksort(right)
print(quicksort([3, 6, 8, 10, 1, 2, 1]))
print()
