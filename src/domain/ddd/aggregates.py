from pydantic.dataclasses import dataclass

from .mixins import BusinessRuleValidationMixin

@dataclass(kw_only=True)
class AggregateRoot(BusinessRuleValidationMixin):
    pass
