# Непубличные члены класса и свойства класса
# Проблема: что если value должно быть обязатльно больше 100

# "Явский стиль" доступа к непубличным членам
# class Foo:
#
#     def __init__(self, value = 0):
#         self.set_value(value)
#
#     def get_value(self):
#         return self._value
#
#     def set_value(self, value):
#         if value > 100:
#             self._value = value
#         else:
#             raise ValueError("ERR > 100")

# Создание свойства у класса с помощью функции property
# Хотя, с точки написания клиентсткого кода, нет разницы между полем и свойством,
# но с точки зрения класса (и того, как он работает) разница большая
# class Foo:
#
#     def __init__(self, value = 0):
#         self.set_value(value)
#
#     def get_value(self):
#         return self._value
#
#     def set_value(self, value):
#         if value > 100:
#             self._value = value
#         else:
#             raise ValueError("ERR > 100")
#
#     value = property(get_value, set_value)

# Создание свойства у класса с помощью декоратора property
# Хотя, с точки написания клиентсткого кода, нет разницы между полем и свойством,
# но с точки зрения класса (и того, как он работает) разница большая
class Foo:

    def __init__(self, value = 0):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > 100:
            self._value = value
        else:
            raise ValueError("ERR > 100")


foo1 = Foo(123)
# foo1._value = 12 # технически возможно, но это нарушение  "правил приличия"
# print(foo1._value)
# foo1.set_value(12)
# print(foo1.get_value())

foo1.value = 1234
print(foo1.value)
