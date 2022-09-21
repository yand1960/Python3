import re

passport = "12 34 567890aaa"

# valid = True
#
# if len(passport) != 12:
#     valid = False
#
# if passport[2] != " " or passport[5] != " ":
#     valid = False
#
# for i in [0, 1, 3, 4, 6, 7, 8, 9, 10, 11]:
#     if passport[i] < "0" or passport[i] > "9":
#         valid = False
#
# print(valid)

# \d - цифра, \D - НЕ цифра
# {2, 3} - Ровно 2 или 3 раза
# ^ - начало текста, $ - конец текста
pattern = "^\d{2} \d{2} \d{6}$"
result = re.match(pattern, passport)
print(not result is None)

text = """
Мама мыла раму.
Тетя  Даша тащила шпалу.
Тетя Оля отправилась на море.
Дядя Вася тащил шпалу.
Пете 8 лет.
Тётя Глаша тащила шпалу.
Дядя Коля тащил сома из реки.
"""

# Как зовут теть, которые тащили шпалу?
# \s - пробельный символ, \S - непробельный символ
# + - в любом количестве
# [её] - е или ё
# (...) - группа, которая нас интересует
pattern = "Т[её]тя\s+(\S+) тащила шпалу"
result = re.findall(pattern, text)
print(result)

# Как зовут всех, кто тащил шпалу? (9:45)
pattern = "(\S+) тащила{0,1} шпалу"
result = re.findall(pattern, text)
print(result)
