from decision import Decision

class DecisionQuery(Decision):
    def __init__(self):
        self.title = ""
        self.positive = None
        self.negative = None
        self.test = None

    def evaluate(self, entity):
        user = entity
        if self.test(user):
            self.positive.evaluate(user)
        else:
            self.negative.evaluate(user)