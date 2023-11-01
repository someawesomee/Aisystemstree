from abc import ABC, abstractmethod
class Client:
    def __init__(self):
        self.ecgResult = False
        self.Years = 0
        self.ChestPain = False
        self.BloodPressure = False

    @property
    def ecgResult(self):
        return self._ecgResult

    @ecgResult.setter
    def ecgResult(self, value):
        self._ecgResult = value
    
    @property
    def Years(self):
        return self._Years

    @Years.setter
    def Years(self, value):
        self._Years = value
    
    @property
    def ChestPain(self):
        return self._ChestPain

    @ChestPain.setter
    def ChestPain(self, value):
        self._ChestPain = value

    @property
    def BloodPressure(self):
        return self._BloodPressure

    @BloodPressure.setter
    def BloodPressure(self, value):
        self._BloodPressure = value

        

   

class Decision(ABC):
    @abstractmethod
    def evaluate(self, client):
        pass
