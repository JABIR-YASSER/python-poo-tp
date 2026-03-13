class AlbumMusical:
    def __init__(self, titre, genre, annee):
        self.__titre = titre
        self.__genre = genre
        self.__annee = annee
        
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
    def annee(self):
        return self._annee
    
    @annee.setter
    def annee(self, value):
        self.__annee = value
        
    def afficher(self):
        print(f"Album: Titre - {self.titre}, Genre - {self.genre}, Année - {self.annee}")
    
    def __str__(self):
        return f"Album: {self.titre} ({self.annee}) - {self.genre}"


class Musicien:
    def __init__(self, ID, nom):
        self.__ID = ID
        self.__nom = nom
        self.__albums = []
    
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
    def albums(self):
        return self.__albums
    
    def afficher(self):
        print(f"Musicien ID: {self.ID}, Nom: {self.nom}")
        print("Discographie:")
        for album in self.albums:
            album.afficher()
    
    def __str__(self):
        return f"Musicien: {self.nom} (ID: {self.ID})"
    
    def ajouter(self, album):
        self.albums.append(album)
    
    def chercher(self, titre):
        for album in self.albums:
            if album.titre == titre:
                return album
        return None
    
    def supprimer(self, titre):
        album = self.chercher(titre)
        if album:
            self.albums.remove(album)
            print(f"L'album '{titre}' a été supprimé.")
        else:
            print(f"L'album '{titre}' n'existe pas dans la discographie.")
    
    def modifier(self, titre, nouveau_genre, nouvelle_annee):
        album = self.chercher(titre)
        if album:
            album.genre = nouveau_genre
            album.annee = nouvelle_annee
            print(f"Les informations de l'album '{titre}' ont été modifiées.")
        else:
            print(f"L'album '{titre}' n'existe pas dans la discographie.")


if __name__ == "__main__":
    musicien = Musicien(1, "John Doe")
    
    album1 = AlbumMusical("Album A", "Rock", 2000)
    album2 = AlbumMusical("Album B", "Pop", 2010)
    musicien.ajouter(album1)
    musicien.ajouter(album2)
    
    while True:
        print("\nMenu:")
        print("1. Ajouter un album")
        print("2. Afficher les détails du musicien et sa discographie")
        print("3. Chercher un album par titre")
        print("4. Supprimer un album")
        print("5. Modifier un album")
        print("6. Quitter")
        
        choix = input("Entrez votre choix: ")
        
        if choix == '1':
            titre = input("Titre de l'album: ")
            genre = input("Genre de l'album: ")
            annee = input("Année de l'album: ")
            album = AlbumMusical(titre, genre, annee)
            musicien.ajouter(album)
            print("Album ajouté avec succès.")
        
        elif choix == '2':
            musicien.afficher()
        
        elif choix == '3':
            titre = input("Titre de l'album à chercher: ")
            album = musicien.chercher(titre)
            if album:
                print("Album trouvé:")
                album.afficher()
            else:
                print("Album non trouvé.")
        
        elif choix == '4':
            titre = input("Titre de l'album à supprimer: ")
            musicien.supprimer(titre)
        
        elif choix == '5':
            titre = input("Titre de l'album à modifier: ")
            nouveau_genre = input("Nouveau genre: ")
            nouvelle_annee = input("Nouvelle année: ")
            musicien.modifier(titre, nouveau_genre, nouvelle_annee)
        
        elif choix == '6':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")