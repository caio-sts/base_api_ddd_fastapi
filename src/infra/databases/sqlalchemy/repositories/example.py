from typing import Optional

from sqlalchemy import select

from src.application.repositories.example import ExampleRepository
from src.infra.databases.sqlalchemy.adapters.example import ExampleAdapter
from src.domain.example import Example
from src.infra.databases.sqlalchemy.connection import Session
from src.infra.databases.sqlalchemy.entities.example import (
    Example as ExampleEntity,
)


class ExampleRepositoryDatabase(ExampleRepository):

    def __init__(self) -> None:
        self.__session = Session

    def get_all(self) -> Optional[Example]:
        # NOTE: Fluxo normal
        # stmt = select(ExampleEntity)
        # try:
        #     examples = self.__session.query(ExampleEntity).scalars().unique()

        #     return ExampleAdapter.entity_to_model(examples)
        # except Exception as e:
        #     print(f"ExceptionError: {e}")
        #     raise e

        # NOTE: Fluxo simulado
        examples = [Example(id=1, name="ABCD")]

        # retorno do banco
        example_entities = [ExampleAdapter.model_to_entity(model) for model in examples]

        # voltando para o domínio
        return [ExampleAdapter.entity_to_model(entity) for entity in example_entities]