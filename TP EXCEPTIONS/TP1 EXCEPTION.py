
class InsufficientFundsError(Exception):
    pass

class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire
        self.__solde = solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif et non nul.")
        self.__solde += montant
        print(f"Dépôt de {montant}€ effectué. Nouveau solde : {self.__solde}€.")

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif et non nul.")
        if montant > self.__solde:
            raise InsufficientFundsError("Solde insuffisant pour effectuer ce retrait.")
        self.__solde -= montant
        print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.__solde}€.")

    def afficher_solde(self):
        print(f"Solde actuel du compte de {self.__titulaire} : {self.__solde}€.")

if __name__ == "__main__":
    compte = CompteBancaire("Anass", 1000)
    compte.afficher_solde()

    try:
        compte.deposer(500)
        compte.retirer(1000)
        compte.retirer(2000)
    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except InsufficientFundsError as ife:
        print(f"Erreur de solde insuffisant : {ife}")
    finally:
        compte.afficher_solde()
