from ..dal.repository_csv import RepositoryCsv


class Calculations:

    def __init__(self, connectionString):
        self.repository = RepositoryCsv(connectionString)

    def plus(self, x: int, y: int) -> int:
        result = x + y
        self.repository.add(x, y, "plus", result)
        return result

    def minus(self, x: int, y: int) -> int:
        result = x - y
        self.repository.add(x, y, "minus", result)
        return result