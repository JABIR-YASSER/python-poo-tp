class Adresse:
    def __init__(self, ville, pays):
        self.__ville = ville
        self.__pays = pays
    ####################################
    @property
    def ville(self):
        return self.__ville
    
    @ville.setter
    def ville(self, ville):
        self.__ville = ville
    ####################################
    @property
    def pays(self):
        return self.__pays

    @pays.setter
    def pays(self, pays):
        self.__pays = pays
    ####################################
    def afficher(self):
        print(f"Ville: {self.__ville}, Pays: {self.__pays}")

    def __str__(self):
        return f"Adresse: {self.__ville}, {self.__pays}"

########################################################################
class Fabriquant:
    def __init__(self, nomF, adresse):
        self.__nomF = nomF
        self.__adresse = adresse
    ####################################
    @property
    def nomF(self):
        return self.__nomF

    @nomF.setter
    def nomF(self, nom):
        self.__nomF = nom
    ####################################
    @property
    def adresse(self):
        return self.__adresse

    @adresse.setter
    def adresseF(self, adress):
        self.__adresse = adress
    ####################################
    def afficher(self):
        print(f"Nom du Fabriquant: {self.__nomF}")
        self.adresse.afficher()

    def __str__(self):
        ad=self.adresse.__str__()
        return f"Fabriquant: {self.__nomF}, Adresse: {ad}"

########################################################################
class Produit:
    def __init__(self, titre, fab):
        self.__titre = titre
        self.__fab = fab
    ####################################
    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, titre):
        self.__titre = titre
    ####################################
    @property
    def fab(self):
        return self.__fab

    @fab.setter
    def fab(self, fab):
        self.__fab = fab
    ####################################
    def afficher(self):
        print(f"Produit: {self.__titre}")
        self.fab.afficher()

    def __str__(self):
        f=self.fab.__str__()
        return f"Produit: {self.__titre}, Fabriquant: {f}"

########################################################################

if __name__ == "__main__":
    adresse1 = Adresse("Paris", "France")
    adresse2 = Adresse("Berlin", "Allemagne")

    fabriquant1 = Fabriquant("Fabriquant A", adresse1)
    fabriquant2 = Fabriquant("Fabriquant B", adresse2)

    produit1 = Produit("Produit X", fabriquant1)
    produit2 = Produit("Produit Y", fabriquant2)
    
    print("\nAffichage des adresses:")
    adresse1.afficher()
    print(adresse2)
    
    print("\nAffichage des fabriquants:")
    fabriquant1.afficher()
    print(fabriquant2)
    
    print("\nAffichage des produits:")
    print(produit1)
    produit2.afficher()