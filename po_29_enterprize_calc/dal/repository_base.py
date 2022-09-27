from datetime import datetime


class RepositoryBase:

    def add(self, x: int, y: int, operation: str, result: int, timestamp: datetime) -> None:
        pass