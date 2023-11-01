from decision import Decision

class DecisionQuery(Decision):
    def __init__(self, title, test, positive, negative):
        self.title = title
        self.test = test
        self.positive = positive
        self.negative = negative

    def evaluate(self, client):
        result = self.test(client)
        result_as_string = "yes" if result else "no"

        if result:
            self.positive.evaluate(client)
        else:
            self.negative.evaluate(client)
