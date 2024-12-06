from datetime import datetime
from pydantic.dataclasses import dataclass
from .ddd.aggregates import AggregateRoot

@dataclass(kw_only=True)
class Example(AggregateRoot):
    id: int | None = None
    name: str = ""
