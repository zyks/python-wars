from abc import ABCMeta, abstractmethod


class System(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, time):
        pass

    @abstractmethod
    def end(self):
        pass
