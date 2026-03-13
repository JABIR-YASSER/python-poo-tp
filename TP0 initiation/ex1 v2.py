class Etudiant :
    def __init__ (self,id,nom,note,ville):
        self.__id=id
        self.__nom=nom
        self.__note=note
        self.__ville=ville
    ###########################################
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    ###########################################
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    ###########################################
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note):
        self.__note = note
    ###########################################
    @property
    def ville(self):
        return self.__ville
    @ville.setter
    def ville(self, ville):
        self.__ville = ville
    ###########################################
    def afficher(self):
        print(f"ID : {self.__id}")
        print(f"Nom : {self.__nom}")
        print(f"Note : {self.__note}")
        print(f"Ville : {self.__ville}")
    def __str__(self):
        return " le id est : " + str(self.__id) + "\n le nom est : " + self.__nom + "\n la note : "+str(self.__note) +"\n la ville " + self.__ville
#################################################################################################################################   
etudiant1 = Etudiant(1, "Alice", 15.5, "Paris")
etudiant2 = Etudiant(2, "Bob", 12.0, "Lyon")
etudiant1.afficher()
print(etudiant2)
etudiant1.note=17.0
etudiant1.ville='Nice'
print("\nAprès mise à jour des informations de l'étudiant1 :")
print(etudiant1)