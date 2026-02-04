from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController


class Controller(IController):
    __view: IView
    model: IModel

    def __init__(self) -> None:
        self.__view = None
        self.model = None

    def setView(self, view: IView) -> None:
        self.__view =view

    def setModel(self, model: IModel) -> None:
        self.model=model

    def start(self) -> None:
        self.__view.showMessage(f"Partie Initiée ... Le but du jeu est de trouver le nombre magique entre 1 et 100, vous avez donc {self.model.getMaxNumberOfProposals()} tentatives")
        maximumTry = self.model.getMaxNumberOfProposals()

        while self.model.getProposalCount() < maximumTry:
            proposal = self.__view.askProposal()
            if isinstance(proposal, int):
                self.performProposeNumber(proposal)
            else:
                self.__view.showMessage("Entrée invalide. Veuillez réessayer.")

        self.__view.showMessage(F"Désolé, vous avez épuisé vos {maximumTry} tentatives. Le nombre magique était {self.model._magic_number}.")

    def performProposeNumber(self, num: int) -> None:
        result = self.model.compareToMagicNumber(num)
        self.__view.showMessage(result)

        if result == "Parfait !":
            self.__view.showMessage(f"Félicitations ! Vous avez trouvé le nombre magique {num} en {self.model.getProposalCount()} tentatives il vous reste donc {self.model.getMaxNumberOfProposals() - self.model.getProposalCount()} tentatives.")
