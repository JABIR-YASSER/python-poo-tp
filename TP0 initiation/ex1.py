class Etudiant :
    def __init__ (self,id,nom,note,ville):
        self.__id=id
        self.__nom=nom
        self.__note=note
        self.__ville=ville
    ###########################################
    def get_identifiant(self):
        return self.__id

    def get_nom(self):
        return self.__nom

    def get_note(self):
        return self.__note

    def get_ville(self):
        return self.__ville
    ###########################################
    def set_identifiant(self, id):
        self.__identifiant = id

    def set_nom(self, nom):
        self.__nom = nom

    def set_note(self, note):
        self.__note = note

    def set_ville(self, ville):
        self.__ville = ville
    ###########################################
    def afficher(self):
        print(f"ID : {self.__id}")
        print(f"Nom : {self.__nom}")
        print(f"Note : {self.__note}")
        print(f"Ville : {self.__ville}")
    def __str__(self):
        return " le id est : " + str(self.__id) + "\n nom est : " + self.__nom + "\n la note : "+str(self.__note) +"\n la ville " + self.__ville
#################################################################################################################################    
etudiant1 = Etudiant(1, "Alice", 15.5, "Paris")
etudiant2 = Etudiant(2, "Bob", 12.0, "Lyon")
etudiant1.afficher()
print(etudiant2)
etudiant1.set_note(17.0)
etudiant1.set_ville("Nice")
print("\nAprès mise à jour des informations de l'étudiant1 :")
etudiant1.afficher()