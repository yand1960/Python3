# Это не совсем типичный класс. Для этого класса бессмысленно понятие объекта
# В других платформах такого рода классы обычно называются статическими
class MyGeometry:

    # Это называется "поле класса". Не совсем точно, "совйство класса"
    non_eqluid = 1.0

    # Это называется "метод класса"
    @classmethod
    def hypot(cls, a, b):
        return ((a * a + b * b) ** 0.5) * MyGeometry.non_eqluid

    @classmethod
    def square(cls, a, b):
        return a * b / 2 * MyGeometry.non_eqluid


# print(hypot(3, 4), square(3, 4))
# Расчет по Эвклиду
print(MyGeometry.non_eqluid)
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))

# Расчет по (якобы) Лобачевскому
MyGeometry.non_eqluid = 0.9
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))

# Расчет по (якобы) Гауссу
MyGeometry.non_eqluid = 1.1
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))
