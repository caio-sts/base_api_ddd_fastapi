from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


# Para que a classe seja persistida, deve herdar de Base
# class Example(Base):
class Example:
    __tablename__ = 'example'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), default="")

    # NOTE: Necessário apenas para o fluxo com adapter funcionar
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    #