from decision import Decision

class DecisionResult(Decision):
    def __init__(self, result):
        self.result = result

    def evaluate(self, client):
        get_result_text = "true" if self.result else "false"
        print(f"{self.title}: {get_result_text}")
