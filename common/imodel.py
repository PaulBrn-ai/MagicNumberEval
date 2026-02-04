from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def compareToMagicNumber(self, num: int) -> int:
        pass

    @abstractmethod
    def getProposalCount(self) -> int:
        pass

    @abstractmethod
    def getMaxNumberOfProposals(self) -> int:
        pass
