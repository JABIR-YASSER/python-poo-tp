class Produit:
    def __init__(self, code, nom, prix, description):
        self.__code = code
        self.__nom = nom
        self.__prix = prix
        self.__description = description
    ###########################################
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code):
        self.__code = code
    ###########################################
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    ##########################################    
    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix):
        self.__prix = prix
    ###########################################
    @property
    def description(self):
        return self.__description
    @description.setter
    def set_description(self, description):
        self.__description = description
    ###########################################
    def afficher(self):
        print(f"Code : {self.__code}")
        print(f"Nom : {self.__nom}")
        print(f"Prix : {self.__prix} €")
        print(f"Description : {self.__description}")
        
    def __str__(self):
        return (f"Code : {self.__code} "+f"\nNom : {self.__nom} "+f"\nPrix : {self.__prix:} € "+f"\nDescription : {self.__description}")
#################################################################################################################################
produit1 = Produit("P001", "Café", 3.6, "Café moulu de qualité supérieure")
produit2 = Produit("P002", "Thé", 2.2, "Thé vert bio en sachets")
produit1.afficher()
produit2.afficher()
produit1.set_prix= 4.00
print("----------")
print("\nAprès mise à jour du prix de produit1 :")
print(f"Prix mis à jour : {produit1.prix} €")
print("----------")
print(produit1)
