class Voiture:
    def __init__ (self,immatriculation,marque,modele):
        self.__immatriculation=immatriculation
        self.__marque=marque
        self.__modele=modele
    @property
    def immatriculation(self):
        return self.__immatriculation
    @immatriculation.setter
    def immatriculation(self, immatriculation):
        self.__immatriculation = immatriculation
    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, marque):
        self.__marque = marque
    @property
    def modele(self):
        return self.__modele
    @modele.setter
    def modele(self, modele):
        self.__modele = modele
    def afficher (self):
        print(f"immatriculation:{self.__immatriculation}\nmarque:{self.__marque}\nmodele:{self.__modele}")
    def __str__(self):
        return (f"immatriculation:{self.__immatriculation}\nmarque:{self.__marque}\nmodele:{self.__modele}")

voitures = []
nb_voitures = int(input ("Combien de voitures voulez-vous ajouter ? "))
for i in range(nb_voitures) :
    immatriculation = input ("Saisir l'immatriculation de la voiture : ")
    marque = input("Saisir la marque de la voiture : ")
    modele = input("Saisir le modèle de la voiture : ")
    voiture = Voiture(immatriculation,marque, modele)
    voitures.append(voiture)

for voiture in voitures:
    print(voiture)