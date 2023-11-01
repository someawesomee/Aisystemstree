from DecisionQuery import DecisionQuery

def tree():
    def ecg():
        ecg = DecisionQuery()
        ecg.title = "Heart Attack Risk"
        ecg.test = lambda client: client.ecg
        ecg.positive = DecisionResult()
        ecg.positive.result = True
        ecg.negative = DecisionResult()
        ecg.negative.result  = age

    def age():
        age  = DecisionQuery()
        age.title = "Age >= 65"
        age.test = lambda client: client.age >= 65
        age.positive = ChestPain()
        age.negative = DecisionResult()
        age.negative.result = False
    def ChestPain():
        ChestPain = DecisionQuery()
        ChestPain.title = "Chest Pain True?"
        ChestPain.test = lambda client: client.ChestPain = 1
        ChestPain.positive = 

    def PressureProblems():
        pass