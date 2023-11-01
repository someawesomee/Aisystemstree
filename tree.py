from DecisionQuery import DecisionQuery
from DecisionResult import DecisionResult


class DecisionTree:
    @staticmethod
    def main_decision_tree():
        # Решение 3
        pressure = DecisionQuery(
            "Имеются ли проблемы с давлением",
            lambda client: client.BloodPressure,  # Заменил "yes" на "no"
            DecisionResult(True),
            DecisionResult(False)
        )

        # Решение 2
        pain = DecisionQuery(
            "Имеется ли боль в груди",
            lambda client: client.ChestPain,
            pressure,
            DecisionResult(False)
        )

        # Решение 1
        age = DecisionQuery(
            "Ваш возраст больше 65",
            lambda client: client.Years > 65,
            DecisionResult(False),
            pain
        )

        # Решение 0
        ecgProblems = DecisionQuery(
            "Проблемы с сердцем по результату экг",
            lambda client: client.ecgResult,
            age,
            DecisionResult(False)
        )

        return ecgProblems
