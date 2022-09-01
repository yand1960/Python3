# динамическое расширение класса и его запрет

class Foo:

    __slots__ = "value", "bubu"

    def __init__(self, value = 0):
        self.value = value


foo1 = Foo(123)
# foo1.valu = 777 # error, если классу добавлены слоты
print(foo1.value)

foo1.bubu = "BUBU!"
# foo1.dohoho = lambda x: print("hoho!") # error, если классу добавлены слоты
print(foo1.bubu, foo1)
# foo1.dohoho(1) # error, если классу добавлены слоты

x = 1
# x.bubu = "BUBU!" # error