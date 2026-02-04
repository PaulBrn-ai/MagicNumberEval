from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController


class Controller(IController):
    # To be completed

    def setView(self, view: IView) -> None:
        pass

    def setModel(self, model: IModel) -> None:
        pass

    def start(self) -> None:
        pass

    def performProposeNumber(self, num: int) -> None:
        pass
