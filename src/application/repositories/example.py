from abc import ABC, abstractmethod

from src.domain.example import Example


class ExampleRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Example]:
        raise NotImplementedError
