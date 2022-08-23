from typing import Callable

def f1(x):
    result = 2 * x
    return result

print(f1(1))

# можно прсвавать переменным (так же как и другие типы данных)
f2 = f1
print(f2)
print(f1 is f2)
print(f2(2))

# Обощенные функции - функции, которые в качестве аргументов могут прпнимать другие функции
def f3(x, f):
    x += 1
    result = f(x)
    return result

def f4(x):
    return x * x

print(f3(3, f1))
print(f3(3, f4))
# Лямбда выражения (эквиваленты двух верхних строк)
print(f3(3, lambda x: 2 * x))
print(f3(3, lambda x: x * x))


def f5(x: int, y: int, f: Callable[[int, int], int]) -> int:
    return f(x , y)

print(f5(1,2, lambda x, y: x + y))
print(f5(1,2, lambda x, y: x - y))

# Применение для фильтрации списка
data = [1, 2, 33, 4, 5, 55]
# results = []
# for x in data:
#     if x > 10:
#         results.append(x)

def select(data, criteria):
    results = []
    for x in data:
        if criteria(x):
            results.append(x)
    return results

print(select(data, lambda x: x > 10))
print(select(data, lambda x: x < 10))

# Применение для трансформации списка
data = [1, 2, 33, 4, 5, 55]
# results = []
# for x in data:
#     results.append(2 * x)
# print(results)
# print([2 * x for x in data])

def transform(data: list[any], converter: Callable[[any], any]) -> list[any]:
    results = []
    for x in data:
        results.append(converter(x))
    return results

print(transform(data, lambda x: 2 * x))
print(transform(data, lambda x: x * x))
print(transform(data, lambda x: x * x * x))

words = ['qwerty', 'abcd', 'hello']

print(transform(words, lambda w: w[0].upper() + w[1:]))

# Не надо изобретать велосипеды. Импользование стандратных функций Питона
# для трансформации, фильтрации и сортировки "списков" (Iterables)
data = [1, 2, 33, 4, 5, 55, 6]
results = list(map(lambda x: 2 * x, data))
print(results)
results = list(map(lambda x: x * x, data))
print(results)

results = list(filter(lambda x: x > 10, data))
print(results)

data1 = [(1, 1) , (2, 2), (3, 33), (4, 4), (5, 55)]
# отфильтровать только те члены списка data1, у которых второй член кортежа больше 10
# 10:25

results = list(filter(lambda x: x[1] > 10, data1))
print(results)

print(sorted(data))
print(sorted(data1, key = lambda x: x[1], reverse = True))

people = [
    {
        "firstName": "Yuri",
        "lastName": "Andrienko",
        "salary": 123456,
    },
    {
        "firstName": "Vasya",
        "lastName": "Pupkin",
        "salary": 77777,
        "children": [
            {"name": "Ariadna", "gender": "f"},
            {"name": "David", "gender": "m"},
        ]
    },
    {
        "firstName": "Masha",
        "lastName": "Mashkina",
        "salary": 300000,
    },
]

# 1. Отсортировать people по убыванию зарплаты
# 2. Одной строкой кода вывести фамилию самого высокооплачиваемого сотрудника
# 10:50
print(sorted(people, key= lambda p: -p['salary']))
print(sorted(people, key= lambda p: -p['salary'])[0]['lastName'])
