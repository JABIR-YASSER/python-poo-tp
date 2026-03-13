from datetime import datetime, timedelta
class Article:
    def __init__(self, numero_serie=None, prix_ht=None, quantite_stock=None, quantite_minimale=None):
        self.numero_serie = numero_serie
        self.prix_ht = prix_ht
        self.quantite_stock = quantite_stock
        self.quantite_minimale = quantite_minimale

    def afficher(self):
        print(f"Numéro de série: {self.numero_serie}")
        print(f"Prix HT: {self.prix_ht}")
        print(f"Quantité en stock: {self.quantite_stock}")
        print(f"Quantité minimale: {self.quantite_minimale}")

    def approvisionner(self, qte):
        self.quantite_stock += qte
        print(f"Stock approvisionné de {qte}. Nouvelle quantité en stock: {self.quantite_stock}")

    def achat(self, qte):
        if qte > self.quantite_stock:
            print("Quantité demandée non disponible en stock.")
        else:
            self.quantite_stock -= qte
            print(f"Achat de {qte} effectué. Nouvelle quantité en stock: {self.quantite_stock}")
            if self.quantite_stock < self.quantite_minimale:
                print("Attention: le stock est en dessous de la quantité minimale!")
class Habit(Article):
    def __init__(self, numero_serie=None, prix_ht=0.0, quantite_stock=0, quantite_minimale=0, taille="", couleur=""):
        super().__init__(numero_serie, prix_ht, quantite_stock, quantite_minimale)
        self.taille = taille
        self.couleur = couleur

    def afficher(self):
        super().afficher()
        print(f"Taille: {self.taille}")
        print(f"Couleur: {self.couleur}")
class Electromenager(Article):
    def __init__(self, numero_serie=None, prix_ht=0.0, quantite_stock=0, quantite_minimale=0, poids=0.0, duree_garantie=0):
        super().__init__(numero_serie, prix_ht, quantite_stock, quantite_minimale)
        self.poids = poids
        self.duree_garantie = duree_garantie

    def dateFinGarantie(self):
        date_fin = datetime.now() + timedelta(days=self.duree_garantie * 30)
        return date_fin.strftime("%Y-%m-%d")

    def afficher(self):
        super().afficher()
        print(f"Poids: {self.poids} kg")
        print(f"Durée de garantie: {self.duree_garantie} mois")
        print(f"Date de fin de garantie: {self.dateFinGarantie()}")

habit=Habit( numero_serie=55, prix_ht=50.0, quantite_stock=100, quantite_minimale=10, taille="M", couleur="red")

habit.approvisionner(15)
habit.afficher()
electromenager = Electromenager(numero_serie="E456", prix_ht=200.0, quantite_stock=5, quantite_minimale=2, poids=7.5, duree_garantie=24)
electromenager.achat(3)
print(f"Date de fin de garantie: {electromenager.dateFinGarantie()}")
electromenager.afficher()