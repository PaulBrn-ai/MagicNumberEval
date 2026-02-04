from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):
    # To be completed

    def setActionPerformer(self, actionPerformer: IController) -> None:
        pass

    def setModel(self, model: IModel) -> None:
        pass

    def setController(self, model: IController) -> None:
        pass

    def showMessage(self, message: str) -> None:
        pass

    def askProposal(self) -> int:
        pass
