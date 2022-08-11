# people = [
#     ["Yuri", "Andrienko", 123456],
#     ["Vasya", "Pupkin", 77777],
#     ["Masha", "Mashkina", 300000],
# ]
# for p in people:
#     print(f"{p[0]} {p[1]} has salary {p[2]}")
#
#
# person1 = {
#     "firstName": "Yuri",
#     "lastName": "Andrienko",
#     "salary": 123456,
# }
# print(f"{person1['firstName']} {person1['lastName']} has salary {person1['salary']}")

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
    },
    {
        "firstName": "Masha",
        "lastName": "Mashkina",
        "salary": 300000,
    },
]

for p in people:
    print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")

# 1. Найти среднюю зарплату
# 2. Вывести фамилию самого высокооплачиваемого сотрудника (9:45)
summa = 0
for p in people:
    summa += p['salary']
print(f"Average salary is {summa / len(people)}")

richest = people[0]
for p in people:
    if richest['salary'] < p['salary']:
        richest = p
print(f"Most highly paid is {richest['lastName']}")

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

for p in people:
    print(f"{p['lastName']}, {p['firstName']}")
    if "children" in p.keys():
        print("\tChildren:")
        for c in p['children']:
            print(f"\t\t{c['name']}")

print(people[1]['children'][0]['name'])

i = 0
while i < len(people):
    print(people[i]['lastName'])
    i += 1

for p in people:
    if p['salary'] > 100000:
        print(p['firstName'])
        break

person = people[0]
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} - {value}")

nums = (1, 2, 3)
# nums.append(77)
# nums[0] = 11
print(nums)

set1 = {1, 2, 3}
set2 = {2, 2, 3, 4}
set3 = set(nums)
print(set1, set2, set3)
print(set1.intersection(set2))

iterator = iter(nums)
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))