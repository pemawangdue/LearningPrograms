#Factory design pattern example
from abc import ABC, abstractmethod

class Factory(ABC):

    @abstractmethod
    def getDimension(self):
        pass

class ChairA(Factory):

    def getDimension(self):
        return "chair A dimension"

class ChairB(Factory):

    def getDimension(self):
        return "chair B dimension"


class FactoryDriver:

    @staticmethod
    def getChair(chair_type):
        if chair_type == 'ChairA':
            return ChairA
        elif chair_type == 'ChairB':
            return ChairB

if __name__ == '__main__':
    handler = FactoryDriver.getChair('ChairA')
    print(handler().getDimension())
