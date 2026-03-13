class Voiture:
    def __init__(self, matricule, marque, annee):
        self.__matricule = matricule
        self.__marque = marque
        self.__annee = annee
    @property
    def matricule(self):
        return self.__matricule
    @matricule.setter
    def matricule(self, matricule):
        self.__matricule = matricule
        
    @property
    def marque(self):
        return self.__marque
    @marque.setter
    def marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque
    
    @property
    def annee(self):
        return self.__annee
    @annee.setter
    def annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee
        
    def afficher(self):
        print(f"Matricule: {self.matricule}, Marque: {self.marque}, Année: {self.annee}")

    def __str__(self):
        return f"Voiture: Matricule - {self.matricule}, Marque - {self.marque}, Année - {self.annee}"


class Conducteur:
    def __init__(self, ID, nom):
        self.__ID = ID
        self.__nom = nom
        self.__voitures = []
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nouveau_nom):
        self.__nom = nouveau_nom
    
    @property
    def voitures(self):
        return self.__voitures
    @voitures.setter
    def voitures(self, voitures):
        self.__voitures = voitures
    
    def afficher(self):
        print(f"ID: {self.ID}, Nom: {self.nom}")
        print("Voitures:")
        for voiture in self.voitures:
            voiture.afficher()

    def __str__(self):
        voitures_str = "\n".join([str(voiture) for voiture in self.voitures])
        return f"Conducteur ID: {self.ID}, Nom: {self.nom}\nVoitures:\n{voitures_str}"

    def ajouter(self, voiture):
        self.voitures.append(voiture)

    def chercher(self, matricule):
        for voiture in self.voitures:
            if voiture.matricule == matricule:
                return voiture
        return None

    def supprimer(self, matricule):
        voiture = self.chercher(matricule)
        if matricule:
            self.voitures.remove(voiture)
            print(f"La voiture avec le matricule '{matricule}' a été supprimée.")
        else:
            print(f"La voiture avec le matricule '{matricule}' n'existe pas dans la liste des voitures.")

    def modifier(self, matricule, nouvelle_marque, nouvelle_annee):
        voiture = self.chercher(matricule)
        if matricule:
            voiture.marque = nouvelle_marque
            voiture.annee = nouvelle_annee
            print(f"La voiture avec le matricule '{matricule}' a été modifiée avec succès.")
        else:
            print(f"La voiture avec le matricule '{matricule}' n'existe pas dans la liste des voitures.")
'''
conducteurs = []

nbr_conducteurs = int(input("Combien de conducteurs voulez-vous ajouter ? "))
for i in range(nbr_conducteurs):
    conducteur_id = input(f"Entrez l'ID du conducteur {i + 1}: ")
    nom_conducteur = input(f"Entrez le nom du conducteur {i + 1}: ")

    conducteur = Conducteur(conducteur_id, nom_conducteur)

    
    nbr_voitures = int(input(f"Combien de voitures pour le conducteur {nom_conducteur} ? "))
    for j in range(nbr_voitures):
        matricule = input(f"Entrez le matricule de la voiture {j + 1}: ")
        marque = input(f"Entrez la marque de la voiture {j + 1}: ")
        annee = input(f"Entrez l'année de la voiture {j + 1}: ")

        voiture = Voiture(matricule, marque, annee)
        conducteur.ajouter_voiture(voiture)

    conducteurs.append(conducteur)

# Affichage des informations de tous les conducteurs et de leurs voitures
print("\nInformations de tous les conducteurs et de leurs voitures:")
for conducteur in conducteurs:
    conducteur.afficher()
    print()


################################################################


# Tests
voiture1 = Voiture("123ABC", "Toyota", 2020)
voiture2 = Voiture("456DEF", "Honda", 2018)

conducteur = Conducteur(1, "Alice")
conducteur.ajouter(voiture1)
conducteur.ajouter(voiture2)

conducteur.afficher()
conducteur.modifier("123ABC", "Nouvelle Marque", 2021)
conducteur.supprimer("456DEF")
print(conducteur)
'''
if __name__ == "__main__":
    conducteur = Conducteur(1, "Alice")
    
    while True:
        print("\nMenu:")
        print("1. Ajouter une voiture")
        print("2. Afficher les détails du conducteur et ses voitures")
        print("3. Chercher une voiture par matricule")
        print("4. Supprimer une voiture")
        print("5. Modifier une voiture")
        print("6. Quitter")
        
        choix = input("Entrez votre choix: ")
        
        if choix == '1':
            matricule = input("Matricule de la voiture: ")
            marque = input("Marque de la voiture: ")
            annee = input("Année de la voiture: ")
            voiture = Voiture(matricule, marque, annee)
            conducteur.ajouter(voiture)
            print("Voiture ajoutée avec succès.")
        
        elif choix == '2':
            conducteur.afficher()
        
        elif choix == '3':
            matricule = input("Matricule de la voiture à chercher: ")
            voiture = conducteur.chercher(matricule)
            if voiture:
                print("Voiture trouvée:")
                voiture.afficher()
            else:
                print("Voiture non trouvée.")
        
        elif choix == '4':
            matricule = input("Matricule de la voiture à supprimer: ")
            conducteur.supprimer(matricule)
        
        elif choix == '5':
            matricule = input("Matricule de la voiture à modifier: ")
            nouvelle_marque = input("Nouvelle marque: ")
            nouvelle_annee = input("Nouvelle année: ")
            conducteur.modifier(matricule, nouvelle_marque, nouvelle_annee)
        
        elif choix == '6':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")

