from abc import ABC, abstractmethod


class MethodsWithCoins(ABC):
    """ Работа с коинами """

    @abstractmethod
    def minusCoins(self):
        pass

    @abstractmethod
    def plusCoins(self):
        pass

    @abstractmethod
    def getItemFromModel(self):
        pass

    @abstractmethod
    def getCoinsUser(self):
        pass

    @abstractmethod
    def addIntoHistory(self):
        pass

