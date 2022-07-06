from abc import ABC, abstractmethod

class Animals(ABC):
    @abstractmethod
    def __str__() -> str:
        pass

