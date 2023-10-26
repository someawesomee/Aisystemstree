from typing import Union
from decisionResult import DecisionResult
class DecisionQuery:
    def __init__(self, condition: str, results: list[Union[str, DecisionResult]]):
        self.condition = condition
        self.results = results

    def get_condition(self) -> str:
        return self.condition

    def get_results(self) -> list[Union[str, DecisionResult]]:
        return self.results

    def __eq__(self, other: 'DecisionQuery') -> bool:
        if isinstance(other, DecisionQuery):
            return self.condition == other.condition and self.results == other.results
        return False

    def __ne__(self, other: 'DecisionQuery') -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"{self.condition}: {', '.join([str(result) for result in self.results])}"