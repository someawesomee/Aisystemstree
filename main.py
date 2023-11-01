from decision import Client


client_data = Client()
client_data.BloodPressure = input("Имеются ли проблемы с давлением (yes/no): ").strip().lower() == "true"
client_data.ChestPain = input("Имеется ли боль в груди (yes/no): ").strip().lower() == "true"
client_data.Years = int(input("Ваш возраст больше 65 (число): "))
client_data.ecgResult = input("Проблемы с сердцем по результату экг (yes/no): ").strip().lower() == "true"

from tree import DecisionTree

decision_tree = DecisionTree.main_decision_tree()
decision_tree.evaluate(client_data)
