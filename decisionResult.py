from decision import Decision


class DecisionResult(Decision):
    def __init__(self, result):
        self.result = result

    def evaluate(self, client):
        get_result_text = "YES" if self.result else "NO"
        print(f"\nУ вас проблемы с сердцем: {get_result_text}")
