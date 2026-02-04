from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):
    def __init__(self):
        self.__model = None
        self.__controller = None
        self.__actionPerformer = None

    def setActionPerformer(self, actionPerformer: IController) -> None:
        self.__actionPerformer = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def setController(self, controller: IController) -> None:
        self.__controller = controller

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int | tuple[str, int] | str:
        try:
            line = input("Entrez une proposition (1-100) : ")
            value = int(line)

            if 1 <= value <= 100:
                return value

            print("Hors limites ! Veuillez choisir un nombre entre 1 et 100.")
            return self.askProposal()

        except ValueError:
            print("Ce n'est pas un nombre valide.")
            return self.askProposal()