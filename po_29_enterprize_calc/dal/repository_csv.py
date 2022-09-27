from .repository_base import RepositoryBase, datetime


class RepositoryCsv(RepositoryBase):

    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def add(self, x: int, y: int, operation: str, result: int, timestamp: datetime = datetime.now()) -> None:

        with open(self.connection_string, "a", encoding="utf-8") as f:
            f.write(f"{x};{y};{operation};{result};{timestamp}\n")

