class Livre:
    def __init__ (self,auteur,annee_de_pub):
        self.__auteur=auteur
        self.__annee_de_pub=annee_de_pub
        
    @property
    def auteur(self):
        return self.__auteur
    @auteur.setter
    def auteur(self, auteur):
        self.__auteur = auteur
    @property
    def annee_de_pub(self):
        return self.__annee_de_pub
    @annee_de_pub.setter
    def annee_de_pub(self, annee_de_pub):
        self.__annee_de_pub = annee_de_pub

    def afficher (self):
        print(f"auteur:{self.__auteur}\nannee_de_pub:{self.__annee_de_pub}")
    def __str__(self):
        return (f"auteur:{self.__auteur}\nannee_de_pub:{self.__annee_de_pub}")
Livres=[]

nb_livres = int(input ("Combien de livre voulez-vous ajouter ? "))
for i in range(nb_livres) :
    auteur = input ("Saisir l auteur du livre : ")
    annee_de_pub = input("Saisir l annee: ")
    livre = Livre(auteur,annee_de_pub)
    Livres.append(livre)

for Livre in Livres:
    print(Livre)