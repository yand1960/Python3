# класс вроде списка, который принимает только,
# те значения, которфе соответствует заданному критетрию


class ControlledList(list):

    def __init__(self, data=[], criteria=lambda value: True):
        self._criteria = criteria
        for x in data:
            if not self.criteria(x):
                raise ValueError("Данные не соответствуют критерию")
        super().__init__(data)

    @property
    def criteria(self):
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        for x in self:
            if not criteria(x):
                raise ValueError("Существующие данные не соответствуют критерию")
        self._criteria = criteria

    def append(self, x):
        if self.criteria(x):
            super().append(x)
        else:
            raise ValueError("Данные не соответствуют критерию")

    def __setitem__(self, key, value):
        if self.criteria(value):
            super().__setitem__(key, value)
        else:
            raise ValueError("Данные не соответствуют критерию")

    def __iadd__(self, other):
        raise SyntaxError("Данная операция невозможна для этого класса")

    def __add__(self, other):
        raise SyntaxError("Данная операция невозможна для этого класса")


if __name__ == "__main__":
    list1 = ControlledList([21, 221, 2221], lambda x: x > 10)
    # list1 = list1 + [222, 2222] #error
    list1.append(11)
    list1.append(33)
    list1.criteria = lambda x: x > 0
    print(list1)