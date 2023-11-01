from abc import ABC, abstractmethod

class Decision():
    @abstractmethod
    def Evaluate(self, entity):
        raise NotImplementedError