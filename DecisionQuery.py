from decision import Decision



class DecisionQuery:
    def __init__(self, title, test, positive, negative):
        self.title = title
        self.test = test
        self.positive = positive
        self.negative = negative

    def evaluate(self, client):
        if self.test(client):
            self.positive.evaluate(client)
        else:
            self.negative.evaluate(client)
