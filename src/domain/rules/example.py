from ..ddd.rules import BusinessRule


class BusinessRuleToBeFollowed(BusinessRule):
    __message = "Business Rule must be followed"

    name: str

    def is_broken(self) -> bool:
        return bool("rule is being followed")
