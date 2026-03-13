import re
class Personne:
    def __init__(self, nom):
        self.__nom = "Nom non valide constructeur" 
        if self.valider_nom(nom):
            self.__nom = nom       
        
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,nom):        
        if self.valider_nom(nom):
            self.__nom = nom
        else:
            print("Nom non valide setter")
        
    def valider_nom(self, nom):
        regex = '^[A-Za-z]+$'
        return bool(re.match(regex, nom))
        
    def __str__(self):
        return f"Nom:{self.nom}"

nom = input("Nom ?: ")
p=Personne(nom)
nom = input("Nouveau Nom ?: ")
p.nom=nom
print(p)

        
