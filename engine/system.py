from abc import ABCMeta, abstractmethod


class System(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def end(self):
        pass
