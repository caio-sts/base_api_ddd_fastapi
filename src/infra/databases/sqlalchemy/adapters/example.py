from src.domain.example import Example
from src.infra.databases.sqlalchemy.entities.example import (
    Example as ExampleEntity,
)


class ExampleAdapter:
    @staticmethod
    def entity_to_model(entity: ExampleEntity) -> Example:
        return Example(id=entity.id, name=entity.name)

    @staticmethod
    def model_to_entity(model: Example) -> ExampleEntity:
        return ExampleEntity(id=model.id, name=model.name)
