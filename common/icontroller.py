from abc import ABC, abstractmethod


class IController(ABC):
    @abstractmethod
    def performProposeNumber(self, num: int) -> None:
        pass

    @abstractmethod
    def setView(self, view) -> None:
        pass

    @abstractmethod
    def setModel(self, model) -> None:
        pass

