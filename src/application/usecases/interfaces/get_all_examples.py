from abc import ABC, abstractmethod

from src.domain.example import Example


class IGetAllExamples(ABC):
    @abstractmethod
    def execute(self) -> list[Example]:
        raise NotImplementedError
