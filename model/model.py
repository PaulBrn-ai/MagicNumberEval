import random

from common.imodel import IModel


class Model(IModel):
    # To be completed

    def __init__(self):
        self._magic_number = random.randint(1, 100)
        self._proposal_count = 0
        while True:
            try:
                n = int(input("Nombre de tentatives : "))

                if n > 30:
                    print(f"Va te faire voir ! {n} Tentatives ?! C'est beaucoup trop ! Maintenant tu seras puni !!!")
                    n = 5
                    print(f"Testicular Torsion ! {n} tentatives !")

                self._max_proposals = n
                break

            except ValueError:
                # Si l'utilisateur tape "abc" ou "12.4", on tombe ici
                print("Apprends à taper un nombre entier, abruti !")

    def compareToMagicNumber(self, num: int) -> str:
        self._proposal_count += 1
        if num < self._magic_number:
            return "Vise plus haut !"
        elif num > self._magic_number:
            return "Vise plus Bas !"
        else:
            return "Parfait !"

    def getProposalCount(self) -> int:
        return self._proposal_count

    def getMaxNumberOfProposals(self) -> int:
        return self._max_proposals

