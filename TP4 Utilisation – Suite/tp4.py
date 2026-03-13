class JeuVideo:
    def __init__(self, titre, genre, plateforme):
        self.__titre = titre
        self.__genre = genre
        self.__plateforme = plateforme
    
    @property
    def titre(self):
        return self.__titre
    
    @titre.setter
    def titre(self, value):
        self.__titre = value
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, value):
        self.__genre = value
    
    @property
    def plateforme(self):
        return self.__plateforme
    
    @plateforme.setter
    def plateforme(self, value):
        self.__plateforme = value
    def afficher(self):
        print(f"Jeu vidéo: Titre - {self.titre}, Genre - {self.genre}, Plateforme - {self.plateforme}")
    
    def __str__(self):
        return f"Jeu vidéo: {self.titre} ({self.plateforme}) - {self.genre}"


class Developpeur:
    def __init__(self, ID, nom):
        self.__ID = ID
        self.__nom = nom
        self.__portfolio = []
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, value):
        self.__ID = value
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value
    
    @property
    def portfolio(self):
        return self.__portfolio
    
    def afficher(self):
        print(f"developpeur ID: {self.ID}, Nom: {self.nom}")
        print("Portfolio:")
        for jeu in self.portfolio:
            jeu.afficher()
    
    def __str__(self):
        return f"developpeur: {self.nom} (ID: {self.ID})"
    
    def ajouter(self, jeu):
        self.portfolio.append(jeu)
    
    def chercher(self, titre):
        for jeu in self.portfolio:
            if jeu.titre == titre:
                return jeu
        return None
    
    def supprimer(self, titre):
        jeu = self.chercher(titre)
        if jeu:
            self.portfolio.remove(jeu)
            print(f"Le jeu '{titre}' a ete supprimé du portfolio.")
        else:
            print(f"Le jeu '{titre}' n'existe pas dans le portfolio.")
    
    def modifier(self, titre, nouveau_genre, nouvelle_plateforme):
        jeu = self.chercher(titre)
        if jeu:
            jeu.genre = nouveau_genre
            jeu.plateforme = nouvelle_plateforme
            print(f"Les informations du jeu '{titre}' ont ete modifiées.")
        else:
            print(f"Le jeu '{titre}' n'existe pas dans le portfolio.")


class Societe:
    def __init__(self, rc):
        self.rc = rc
        self.developpeurs = []
    
    def afficher(self):
        print(f"Societe RC: {self.rc}")
        print("Developpeurs:")
        for dev in self.developpeurs:
            print(dev)
    
    def __str__(self):
        return f"Societe RC: {self.rc}"
    
    def ajouter(self, developpeur):
        self.developpeurs.append(developpeur)
    
    def chercher(self, ID):
        for dev in self.developpeurs:
            if dev.ID == ID:
                return dev
        return None
    
    def supprimer(self, ID):
        developpeur = self.chercher(ID)
        if developpeur:
            self.developpeurs.remove(developpeur)
            print(f"Le developpeur avec l'ID {ID} a ete supprimé de la Societe.")
        else:
            print(f"Le developpeur avec l'ID {ID} n'existe pas dans la Societe.")
    
    def modifier(self, ID, nouveau_nom):
        developpeur = self.chercher(ID)
        if developpeur:
            developpeur.nom = nouveau_nom
            print(f"Le nom du developpeur avec l'ID {ID} a ete modifié.")
        else:
            print(f"Le developpeur avec l'ID {ID} n'existe pas dans la Societe.")


if __name__ == "__main__":
    societe = Societe("00")
    
    dev1 = Developpeur(1, "yasser")
    dev2 = Developpeur(2, "jbira")
    jeu1 = JeuVideo("Jeu A", "a", "PC")
    jeu2 = JeuVideo("Jeu B", "b", "PS5")
    dev1.ajouter(jeu1)
    dev2.ajouter(jeu2)
    societe.ajouter(dev1)
    societe.ajouter(dev2)
    
    while True:
        print("\nMenu:")
        print("1. Ajouter un developpeur")
        print("2. Afficher les informations de la Societe et les Developpeurs")
        print("3. Chercher un developpeur par ID")
        print("4. Supprimer un developpeur")
        print("5. Modifier le nom d'un developpeur")
        print("6. Quitter")
        
        choix = input("Entrez votre choix: ")
        
        if choix == '1':
            ID = int(input("Entrez l'ID du developpeur: "))
            nom = input("Entrez le nom du developpeur: ")
            nouveau_developpeur = Developpeur(ID, nom)
            societe.ajouter(nouveau_developpeur)
            print("developpeur ajouté avec succès.")
        
        elif choix == '2':
            societe.afficher()
        
        elif choix == '3':
            ID = int(input("Entrez l'ID du developpeur à chercher: "))
            developpeur = societe.chercher(ID)
            if developpeur:
                print("developpeur trouvé:")
                developpeur.afficher()
            else:
                print("developpeur non trouvé.")
        
        elif choix == '4':
            ID = int(input("Entrez l'ID du developpeur à supprimer: "))
            societe.supprimer(ID)
        
        elif choix == '5':
            ID = int(input("Entrez l'ID du developpeur à modifier: "))
            nouveau_nom = input("Entrez le nouveau nom du developpeur: ")
            societe.modifier(ID, nouveau_nom)
        
        elif choix == '6':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")