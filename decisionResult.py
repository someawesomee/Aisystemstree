class DecisionResult:
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: 'DecisionResult') -> bool:
        return self.value == other.value

    def __ne__(self, other: 'DecisionResult') -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: 'DecisionResult') -> bool:
        return self.value < other.value

    def __le__(self, other: 'DecisionResult') -> bool:
        return self.value <= other.value

    def __ge__(self, other: 'DecisionResult') -> bool:
        return self.value >= other.value

    def __gt__(self, other: 'DecisionResult') -> bool:
        return self.value > other.value

    def __ge__(self, other: 'DecisionResult') -> bool:
        return self.value >= other.value

    def __add__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value + other.value)

    def __sub__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value - other.value)

    def __mul__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value * other.value)

    def __truediv__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value / other.value)

    def __radd__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value + other.value)

    def __rsub__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value - other.value)

    def __rmul__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value * other.value)

    def __rtruediv__(self, other: 'DecisionResult') -> 'DecisionResult':
        return DecisionResult(self.value / other.value)

    def __r__ (self, other: 'DecisionResult') -> bool:
        return self.value == other.value