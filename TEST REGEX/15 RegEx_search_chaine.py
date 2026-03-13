import re
class Personne:
    def __init__(self, adresse):
        self.__adresse = "Adresse non valide" 
        if self.valider_adresse(adresse):
            self.__adresse = adresse       
        
    @property
    def adresse(self):
        return self.__adresse
    
    @adresse.setter
    def adresse(self,adresse):        
        if self.valider_adresse(adresse):
            self.__adresse = adresse
        else:
            print("Adresse non valide")
        
    def valider_adresse(self, adresse):
        regex = "casa"
        return bool(re.search(regex, adresse))
        
    def __str__(self):
        return f"Adresse:{self.adresse}"

adresse = input("Adresse ?: ")
p=Personne(adresse)
print(p)

        
