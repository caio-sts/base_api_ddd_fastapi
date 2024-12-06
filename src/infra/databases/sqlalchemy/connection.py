from decouple import config
from sqlalchemy import create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from src.infra.databases.sqlalchemy.entities.base import Base
from src.infra.databases.sqlalchemy.entities.example import Example


url = URL.create(
    drivername=config("DATABASE_DRIVER"),
    username=config("DATABASE_USER"),
    password=config("DATABASE_PASSWORD"),
    host=config("DATABASE_HOST"),
    port=config("DATABASE_PORT"),
    database=config("DATABASE_TEST_NAME")
        if config("DEV_MODE").lower() == "true"
        else config("DATABASE_NAME"),
)

engine = create_engine(url, echo=False)
Session = scoped_session(sessionmaker(bind=engine))


def init_database():
    Base.metadata.create_all(engine)
    if config("DEV_MODE")=="true":
        pass
        # NOTE: Se quiser iniciar o banco com dados, modifique
        # a função put_initial_data e descomente abaixo
        # put_initial_data()

def put_initial_data():
    with Session() as session:
        # Example
        query = select("*").select_from(Example)
        result = session.execute(query).fetchall()
        if not result:
            example = {
                "name": "Example",
            }
            session.add(Example(**example))
            session.commit()
