
class Produit:
    def __init__ (self,num_serie,intitule,date_production,prix,nom_producteur):
        self.__num_serie=num_serie
        self.__intitule=intitule
        self.__date_production=date_production
        self.__prix=prix
        self.__nom_producteur=nom_producteur
        self.__distributeurs = []
    def ajouter_distributeurs(self, distributeurs):
        self.distributeurs.append(distributeurs)
    @property
    def num_serie(self):
        return self.__num_serie
    @num_serie.setter
    def num_serie(self, num_serie):
        self.__num_serie = num_serie
    @property
    def intitule(self):
        return self.__intitule
    @intitule.setter
    def intitule(self, intitule):
        self.__intitule = intitule
    @property
    def distributeurs(self):
        return self.__distributeurs
    @distributeurs.setter
    def distributeurs(self, distributeurs):
        self.__distributeurs = distributeurs
    @property
    def date_production(self):
        return self.__date_production
    @date_production.setter
    def date_production(self, date_production):
        self.__date_production = date_production
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix):
        self.__prix = prix
    @property
    def nom_producteur(self):
        return self.__nom_producteur
    @nom_producteur.setter
    def nom_producteur(self, nom_producteur):
        self.__nom_producteur = nom_producteur
    def afficher (self):
        print(f"num_serie:{self.__num_serie}\nintitule:{self.__intitule}\nliste_distributeurs:{self.__distributeurs}\ndate_production:{self.__date_production}\nprix:{self.__prix}\nnom_producteur:{self.__nom_producteur}")
    def __str__(self):
        return (f"num_serie:{self.__num_serie}\nintitule:{self.__intitule}\nliste_distributeurs:{self.__distributeurs}\ndate_production:{self.__date_production}\nprix:{self.__prix}\nnom_producteur:{self.__nom_producteur}")
    def remise(self,taux):
        self.__prix-=(self.__prix * taux/100)
    
liste_produits = []
nombre = int(input("Donner le nombre de produits : "))

for i in range(nombre):
    num_serie = int(input("Donner le num_serie du produit : "))
    intitule = input("Donner le intitule du produit : ")
    date_production = input("Donner la date de production du produit : ")
    prix = float(input("Donner le prix du produit : "))
    nom_producteur =input("Donner le nom de producteur du produit : ")
    produit = Produit(num_serie,intitule,date_production,prix,nom_producteur)

    nbr_distributeurs= int(input(f"Combien de distributeurs pour le produit {intitule} ? "))
    for n in range(nbr_distributeurs):
        dis = input(f"Entrer la distributeur {n+1} : ")
        produit.ajouter_distributeurs(dis)

    liste_produits.append(produit)
print("--------------------------------")
for produit in liste_produits:
    print(produit)
print("--------------------------------")

taux_remise=float(input("donner le taux de remise:"))
for produit in liste_produits:  
    print(f"prix avant remise pour{produit.intitule} : {produit.prix}dh")
    produit.remise(taux_remise)
    print(f"prix apres remise de{taux_remise} : {produit.prix}dh")
    print("--------------------------------")

distributeurs=input("donner le distributeurs pour afficher le produit:")
for produit in liste_produits:
    if distributeurs:
        print(produit)