# Это типичный класс. Для этого класса важно понятие объекта
class MyGeometry:

    # Это называется "конструктор"
    def __init__(self, non_eqluid: float = 1.0):
        # Это называется "поле класса". В данном случае оно относится не к классу в целом,
        # а к экземляру класса
        self.non_eqluid = non_eqluid

    # Это называется "метод класса", который относится не к классу в целом,
    # а к экземляру класса
    def hypot(self, a, b):
        return ((a * a + b * b) ** 0.5) * self.non_eqluid

    def square(self, a, b):
        return a * b / 2 * self.non_eqluid


# Создаем экземпляры классов
geometry1 = MyGeometry()
geometry2 = MyGeometry(non_eqluid=0.9)
# geometry2.non_eqluid = 0.9
geometry3 = MyGeometry(non_eqluid=1.1)
# geometry3.non_eqluid = 1.1

# print(hypot(3, 4), square(3, 4))
# Расчет по Эвклиду
print(geometry1.hypot(3, 4), geometry1.square(3, 4))

# Расчет по (якобы) Лобачевскому
print(geometry2.hypot(3, 4), geometry2.square(3, 4))

# Расчет по (якобы) Гауссу
print(geometry3.hypot(3, 4), geometry3.square(3, 4))
