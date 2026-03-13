class Livre:
    def __init__ (self,titre,genre):
        self.__titre=titre
        self.__genre=genre
    ######################################
    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, titre):
        self.__titre = titre
    ######################################
    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    ######################################
    def afficher (self):
        print(f"rue:{self.__titre}\ngenre:{self.__genre}")
    def __str__(self):
        return (f"titre:{self.__titre}\nville:{self.__genre}")
############################################################################
class Auteur:
    def __init__(self, ID, nom, livre):
        self.ID = ID
        self.nom = nom
        self.livre = livre
    ######################################
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, value):
        self.__ID = value
    ######################################
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value
    ######################################
    @property
    def livre(self):
        return self.__livre
    
    @livre.setter
    def livre(self, value):
        self.__livre = value
    ######################################
    def afficher(self):
        print(f"ID: {self.ID}, Nom: {self.nom}")
        self.livre.afficher()

    def __str__(self):
        return f"Auteur: {self.nom} (ID: {self.ID}, Livre: {self.livre.titre})"
############################################################################
livre1 = Livre("Harry Potter", "Fantasy")
auteur1 = Auteur(1, "J.K. Rowling", livre1)

print("Affichage du livre:")
livre1.afficher()

print("\nAffichage de l'auteur:")
auteur1.afficher()
auteur1.nom = "Joanne Rowling"
livre1.genre = "Fantasy / Young Adult"

print("\nAprès modification:")
print(livre1)
print(auteur1)
    
    