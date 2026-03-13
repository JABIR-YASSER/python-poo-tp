class Film:
    def __init__(self, titre, realisateur):
        self.__titre = titre
        self.__realisateur = realisateur

    @property
    def titre(self):
        return self.__titre
    @titre.setter
    def titre(self, titre):
        self.__titre = titre

    @property
    def realisateur(self):
        return self.__realisateur
    @realisateur.setter
    def realisateur(self, realisateur):
        self.__realisateur = realisateur

    def afficher(self):
        print(f"Titre: {self.__titre}, Réalisateur: {self.__realisateur}")

    def __str__(self):
        return f"Film: {self.__titre}\nRéalisateur: {self.__realisateur}"


class Acteur:
    def __init__(self, ID, nom):
        self.__ID = ID
        self.__nom = nom
        self.__films = []

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
    def nom(self, nom):
        self.__nom = nom
    
    @property
    def films(self):
        return self.__films
    @films.setter
    def films(self, films):
        self.__films = films
    
    def afficher(self):
        print(f"ID: {self.__ID}, Nom: {self.__nom}")
        print("Films:")
        for film in self.films:
            film.afficher()

    def __str__(self):
        films_str = "\n".join([str(film) for film in self.films])
        return f"Acteur ID: {self.__ID}\nNom: {self.__nom}\nFilms:\n{films_str}"

    def ajouter(self, film):
        self.films.append(film)

    def chercher(self, titre):
        for film in self.films:
            if film.titre == titre:
                return film
        return None

    def supprimer(self, titre):
        film = self.chercher(titre)
        if film:
            self.films.remove(film)
            print(f"Le film '{titre}' a été supprimé.")
        else:
            print(f"Le film '{titre}' n'existe pas dans la liste.")

    def modifier(self, titre, nouveau_realisateur):
        film = self.chercher(titre)
        if film:
            film.realisateur = nouveau_realisateur
            print(f"Le réalisateur du film '{titre}' a été modifié.")
        else:
            print(f"Le film '{titre}' n'existe pas dans la liste.")
''''
nb_acteurs = int(input("Combien d'acteurs souhaitez-vous ajouter ? "))
acteurs = []
for i in range(nb_acteurs):
    nom_acteur = input(f"Entrez le nom de l'acteur {i+1}: ")
    acteur = Acteur(i+1, nom_acteur)

    nb_films = int(input(f"Combien de films l'acteur {nom_acteur} a-t-il joué ? "))
    for j in range(nb_films):
        titre = input(f"Entrez le titre du film {j+1} : ")
        realisateur = input(f"Entrez le réalisateur du film {j+1} : ")
        acteur.ajouter(Film(titre, realisateur))

    acteurs.append(acteur)
#######################################################################################################
print("\nInformations de tous les acteurs et de leurs films:")
for acteur in acteurs:
    acteur.afficher()
'''
film1 = Film("Titre1", "Realisateur1")
film2 = Film("Titre2", "Realisateur2")

acteur1 = Acteur(1, "Acteur1")
acteur1.ajouter(film1)
acteur1.ajouter(film2)

print("Affichage de l'acteur et de ses films:")
acteur1.afficher()

print("\nRecherche d'un film:")
film_recherche = acteur1.chercher("Titre1")
if film_recherche:
    print(film_recherche)
else:
    print("Film non trouvé.")

print("\nSuppression d'un film:")
acteur1.supprimer("Titre1")
print(acteur1)

print("\nModification du réalisateur d'un film:")
acteur1.modifier("Titre2", "NouveauRealisateur")
print(acteur1)