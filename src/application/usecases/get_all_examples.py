from dependency_injector.wiring import inject

from src.application.repositories.example import ExampleRepository
from src.application.usecases.interfaces.get_all_examples import IGetAllExamples


class GetAllExamples(IGetAllExamples):
    @inject
    def __init__(
        self,
        example_repository: ExampleRepository,
    ):
        self.example_repository = example_repository

    def execute(self):
        return self.example_repository.get_all()
