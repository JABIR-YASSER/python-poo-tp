class Film:
    def __init__(self, titre, realisateur):
        self.titre = titre
        self.realisateur = realisateur

    def afficher(self):
        print("Titre:", self.titre, " Réalisateur:", self.realisateur)

    def __str__(self):
        return f"Titre: {self.titre}, Réalisateur: {self.realisateur}"


class Acteur:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.films = []

    def afficher(self):
        print("Id:", self.id, " Nom:", self.nom)
        print("Films:")
        for film in self.films:
            print(film)

    def __str__(self):
        films_str = ', '.join([str(film) for film in self.films])
        return f"Id: {self.id}, Nom: {self.nom}, Films: [{films_str}]"

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


if __name__ == "__main__":
    acteur = Acteur(1, "Said")
    while True:
        print("\nMenu:")
        print("1. Ajouter un film")
        print("2. Afficher les détails de l'acteur et ses films")
        print("3. Chercher un film par titre")
        print("4. Supprimer un film")
        print("5. Modifier le réalisateur d'un film")
        print("6. Quitter")
        
        choix = input("Entrez votre choix: ")
        
        if choix == '1':
            titre = input("Titre du film: ")
            realisateur = input("Réalisateur du film: ")
            film = Film(titre, realisateur)
            acteur.ajouter(film)
            print("Film ajouté avec succès.")
        
        elif choix == '2':
            acteur.afficher()
        
        elif choix == '3':
            titre = input("Titre du film à chercher: ")
            film = acteur.chercher(titre)
            if film:
                print("Film trouvé:", film)
            else:
                print("Film non trouvé.")
        
        elif choix == '4':
            titre = input("Titre du film à supprimer: ")
            acteur.supprimer(titre)
        
        elif choix == '5':
            titre = input("Titre du film à modifier: ")
            nouveau_realisateur = input("Nouveau réalisateur: ")
            acteur.modifier(titre, nouveau_realisateur)
        
        elif choix == '6':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")
