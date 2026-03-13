from abc import ABC, abstractmethod
import json

class Livre(ABC):
    def __init__(self, ISBN, titre, date_acquisition, etat, nbr_pages):
        self._ISBN = ISBN
        self._titre = titre
        self._date_acquisition = date_acquisition
        self._etat = etat  # Doit être "disponible" ou "emprunté"
        self._nbr_pages = nbr_pages

    @property
    def ISBN(self):
        return self._ISBN

    @ISBN.setter
    def ISBN(self, value):
        self._ISBN = value

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._titre = value

    @property
    def date_acquisition(self):
        return self._date_acquisition

    @date_acquisition.setter
    def date_acquisition(self, value):
        self._date_acquisition = value

    @property
    def etat(self):
        return self._etat

    @etat.setter
    def etat(self, value):
        if value.lower() in ["disponible", "emprunté"]:
            self._etat = value.lower()
        else:
            raise ValueError("L'état doit être 'disponible' ou 'emprunté'.")

    @property
    def nbr_pages(self):
        return self._nbr_pages

    @nbr_pages.setter
    def nbr_pages(self, value):
        if value > 0:
            self._nbr_pages = value
        else:
            raise ValueError("Le nombre de pages doit être supérieur à 0.")

    @abstractmethod
    def __str__(self):
        return (f"ISBN: {self.ISBN}, Titre: {self.titre}, Date d'acquisition: {self.date_acquisition}, "
                f"État: {self.etat}, Nombre de pages: {self.nbr_pages}")


class Roman(Livre):
    def __init__(self, ISBN, titre, date_acquisition, etat, nbr_pages, auteur, genre_litteraire):
        super().__init__(ISBN, titre, date_acquisition, etat, nbr_pages)
        self._auteur = auteur
        self._genre_litteraire = genre_litteraire

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, value):
        self._auteur = value

    @property
    def genre_litteraire(self):
        return self._genre_litteraire

    @genre_litteraire.setter
    def genre_litteraire(self, value):
        self._genre_litteraire = value

    def __str__(self):
        return super().__str__() + f", Auteur: {self.auteur}, Genre littéraire: {self.genre_litteraire}"


class Magazine(Livre):
    def __init__(self, ISBN, titre, date_acquisition, etat, nbr_pages, periodicite, sujet_principal):
        super().__init__(ISBN, titre, date_acquisition, etat, nbr_pages)
        self._periodicite = periodicite
        self._sujet_principal = sujet_principal

    @property
    def periodicite(self):
        return self._periodicite

    @periodicite.setter
    def periodicite(self, value):
        self._periodicite = value

    @property
    def sujet_principal(self):
        return self._sujet_principal

    @sujet_principal.setter
    def sujet_principal(self, value):
        self._sujet_principal = value

    def __str__(self):
        return super().__str__() + f", Périodicité: {self.periodicite}, Sujet principal: {self.sujet_principal}"


class BandeDessinee(Livre):
    def __init__(self, ISBN, titre, date_acquisition, etat, nbr_pages, illustrateur):
        super().__init__(ISBN, titre, date_acquisition, etat, nbr_pages)
        self._illustrateur = illustrateur

    @property
    def illustrateur(self):
        return self._illustrateur

    @illustrateur.setter
    def illustrateur(self, value):
        self._illustrateur = value

    def __str__(self):
        return super().__str__() + f", Illustrateur: {self.illustrateur}"

class Bibliotheque:
    def __init__(self, code: str, description: str):
        self._code = code
        self._description = description
        self.livres = []

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    
    def __str__(self):
        return f"Bibliothèque {self.code}: {self.description}, Nombre de livres: {len(self.livres)}"

    def ajouterLivre(self, livre: Livre):
        self.livres.append(livre)

    def rechercheLivre(self, ISBN):
        for livre in self.livres:
            if livre.ISBN == ISBN:
                return livre
        return None


    def ficheInventaire(self):
        for livre in self.livres:
            print(livre)

    def supprimerLivre(self, isbn: str):
        livre = self.rechercheLivre(isbn)
        if livre:
            self.livres.remove(livre)
            return True
        return False


class ReseauDeBibliotheques:
    def __init__(self, nom: str, adresse: str, telephone: str):
        self._nom = nom
        self._adresse = adresse
        self._telephone = telephone
        self.bibliotheques = []

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value
    
    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, value):
        self._adresse = value

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    
    
    def __str__(self):
        return f"Réseau {self.nom}: {len(self.bibliotheques)} bibliothèques."

    def ajouterBibliotheque(self, bibliotheque: Bibliotheque):
        self.bibliotheques.append(bibliotheque)

    def rechercheLivre(self, ISBN):
        for bibliotheque in self.liste_de_bibliotheques:
            livre = bibliotheque.rechercheLivre(ISBN)
            if livre:
                return livre
        return None
    
    def localisation(self, ISBN):
        for bibliotheque in self.bibliotheques:
            livre = bibliotheque.rechercheLivre(ISBN)
            if livre:
                return bibliotheque.description
        return None
    
    def transfererLivre(self, ISBN, bibliotheque_dest):
        for bibliotheque in self.bibliotheques:
            livre = bibliotheque.rechercheLivre(ISBN)
            if livre:
                bibliotheque.supprimerLivre(ISBN)
                bibliotheque_dest.ajouterLivre(livre)
                return True
        return False
    
    
    def exporter(self, nom_fichier):
        data = {
            "reseau": self.nom,
            "adresse": self.adresse,
            "telephone": self.telephone,
            "bibliotheques": [
                {
                    "code": biblio.code,
                    "description": biblio.description,
                    "livres": [vars(livre) for livre in biblio.livres]
                }
                for biblio in self.bibliotheques
            ]
        }
        with open(nom_fichier, 'w') as fichier:
            json.dump(data, fichier, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    reseau = ReseauDeBibliotheques("Réseau Central", "123 Rue Principale", "0123456789")
    roman = Roman("123456", "Les Misérables", "2024-11-28", "disponible", 1500, "Victor Hugo", "Drame")
    magazine = Magazine("789123", "Science et Vie", "2024-01-15", "emprunté", 100, "Mensuel", "Sciences")
    bd = BandeDessinee("456789", "Tintin au Tibet", "2023-12-01", "disponible", 60, "Hergé")
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gérer les bibliothèques")
        print("2. Gérer les livres d'une bibliothèque")
        print("3. Exporter les données du réseau")
        print("4. Quitter")
        choix = input("Entrez votre choix : ")

        if choix == "1":
            while True:
                print("\n--- GESTION DES BIBLIOTHÈQUES ---")
                print("1. Ajouter une bibliothèque")
                print("2. Afficher les bibliothèques")
                print("3. Rechercher un livre dans le réseau")
                print("4. Retour au menu principal")
                choix_biblio = input("Entrez votre choix : ")

                if choix_biblio == "1":
                    code = input("Entrez le code de la bibliothèque : ")
                    description = input("Entrez une description : ")
                    reseau.ajouterBibliotheque(Bibliotheque(code, description))
                    print("Bibliothèque ajoutée avec succès.")
                elif choix_biblio == "2":
                    if not reseau.bibliotheques:
                        print("Aucune bibliothèque dans le réseau.")
                    else:
                        for biblio in reseau.bibliotheques:
                            print(biblio)
                elif choix_biblio == "3":
                    ISBN = input("Entrez l'ISBN du livre à rechercher : ")
                    livre = reseau.rechercheLivre(ISBN)
                    if livre:
                        print("Livre trouvé :")
                        print(livre)
                        print("Localisation :", reseau.localisation(ISBN))
                    else:
                        print("Livre non trouvé dans le réseau.")
                elif choix_biblio == "4":
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.")

        elif choix == "2":
            if not reseau.bibliotheques:
                print("Aucune bibliothèque disponible. Ajoutez-en une d'abord.")
                continue

            print("Liste des bibliothèques :")
            for i, biblio in enumerate(reseau.bibliotheques):
                print(f"{i + 1}. {biblio.description}")
            choix_biblio = int(input("Choisissez une bibliothèque par son numéro : ")) - 1

            if 0 <= choix_biblio < len(reseau.bibliotheques):
                bibliotheque = reseau.bibliotheques[choix_biblio]

                while True:
                    print(f"\n--- GESTION DES LIVRES : {bibliotheque.description} ---")
                    print("1. Ajouter un livre")
                    print("2. Afficher l'inventaire")
                    print("3. Supprimer un livre")
                    print("4. Retour au menu principal")
                    choix_livre = input("Entrez votre choix : ")

                    if choix_livre == "1":
                        print("Quel type de livre voulez-vous ajouter ?")
                        print("1. Roman")
                        print("2. Magazine")
                        print("3. Bande Dessinée")
                        type_livre = input("Entrez votre choix : ")

                        ISBN = input("Entrez l'ISBN : ")
                        titre = input("Entrez le titre : ")
                        date_acquisition = input("Entrez la date d'acquisition : ")
                        etat = input("Entrez l'état (disponible/emprunté) : ")
                        nb_pages = int(input("Entrez le nombre de pages : "))

                        if type_livre == "1":
                            auteur = input("Entrez l'auteur : ")
                            genre = input("Entrez le genre littéraire : ")
                            livre = Roman(ISBN, titre, date_acquisition, etat, nb_pages, auteur, genre)
                        elif type_livre == "2":
                            periodicite = input("Entrez la périodicité : ")
                            sujet_principal = input("Entrez le sujet principal : ")
                            livre = Magazine(ISBN, titre, date_acquisition, etat, nb_pages, periodicite, sujet_principal)
                        elif type_livre == "3":
                            illustrateur = input("Entrez l'illustrateur : ")
                            livre = BandeDessinee(ISBN, titre, date_acquisition, etat, nb_pages, illustrateur)
                        else:
                            print("Choix invalide.")
                            continue

                        bibliotheque.ajouterLivre(livre)
                        print("Livre ajouté avec succès.")
                    elif choix_livre == "2":
                        bibliotheque.ficheInventaire()
                    elif choix_livre == "3":
                        ISBN = input("Entrez l'ISBN du livre à supprimer : ")
                        if bibliotheque.supprimerLivre(ISBN):
                            print("Livre supprimé avec succès.")
                        else:
                            print("Livre non trouvé dans cette bibliothèque.")
                    elif choix_livre == "4":
                        break
                    else:
                        print("Choix invalide. Veuillez réessayer.")
            else:
                print("Choix invalide.")

        elif choix == "3":
            nom_fichier = input("Entrez le nom du fichier pour exporter les données : ")
            reseau.exporter(nom_fichier)
            print(f"Données exportées dans le fichier {nom_fichier}.")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
