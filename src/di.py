from dependency_injector import containers, providers

from src.application.usecases.get_all_examples import GetAllExamples
from src.infra.databases.sqlalchemy.repositories.example import ExampleRepositoryDatabase


class DependencyContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            ".infra.http.routers.example",
        ]
    )

    # Repositories
    example_repository = providers.Singleton(ExampleRepositoryDatabase)


    # Example
    get_all_examples = providers.Factory(GetAllExamples, example_repository=example_repository)