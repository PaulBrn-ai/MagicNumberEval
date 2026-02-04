from abc import ABC, abstractmethod
from common.icontroller import IController
from common.imodel import IModel


class IView(ABC):
    @abstractmethod
    def showMessage(self, message: str) -> None:
        pass

    @abstractmethod
    def setActionPerformer(self, actionPerformer: IController) -> None:
        pass

    @abstractmethod
    def setModel(self, model: IModel) -> None:
        pass

    @abstractmethod
    def setController(self, model: IController) -> None:
        pass

    @abstractmethod
    def askProposal(self) -> int:
        pass