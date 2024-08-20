from bitrix24 import Bitrix24
from abc import ABC, abstractmethod


class Bitrix24Abstract(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def getHook(self):
        pass
