from datetime import datetime

class Joueur:
    def __init__(self, nom, age, position, experimente):
        self._nom = nom
        self._age = self._valider_age(age)
        self._position = position
        self._experimente = experimente

    def _valider_age(self, age):
        while age <= 0: 
            print("Erreur: L'âge doit être un nombre positif.")
            age = int(input("Veuillez entrer un âge valide: "))
        return age

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._valider_age(value)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def experimente(self):
        return self._experimente

    @experimente.setter
    def experimente(self, value):
        self._experimente = value

    def CalculerPrime(self, interne, externe):
        prime = interne * 20000 + externe * 30000
        if self.experimente:
            prime += prime * 0.5 
        return prime

    def __str__(self):
        return f"Joueur: {self.nom}, Âge: {self.age}, Position: {self.position}, Expérimenté: {self.experimente}"


class International(Joueur):
    def __init__(self, nom, age, position, experimente, cumul_annees):
        super().__init__(nom, age, position, experimente)
        self._cumul_annees = self._valider_cumul_annees(cumul_annees)

    def _valider_cumul_annees(self, cumul_annees):
        while cumul_annees >= self.age or cumul_annees < 0:
            print(f"Erreur: Le cumul d'années ({cumul_annees}) est invalide (doit être positif et inférieur à l'âge {self.age}).")
            cumul_annees = int(input("Veuillez entrer un cumul valide: "))
        return cumul_annees

    @property
    def cumul_annees(self):
        return self._cumul_annees

    @cumul_annees.setter
    def cumul_annees(self, value):
        self._cumul_annees = self._valider_cumul_annees(value)

    def CalculerPrime(self, interne, externe):
        prime_joueur = super().CalculerPrime(interne, externe)
        prime_international = prime_joueur + (5000 * self.cumul_annees)
        return prime_international

    def __str__(self):
        return (f"International: {self.nom}, Âge: {self.age}, Position: {self.position}, "
                f"Expérimenté: {self.experimente}, Cumul années: {self.cumul_annees}")



class Entraineur:
    def __init__(self, nom, date_fin_contrat, nb_annees_contrat, prime_annuelle):
        self._nom = nom
        self._date_fin_contrat = date_fin_contrat
        self._nb_annees_contrat = nb_annees_contrat
        self._prime_annuelle = self._valider_prime_annuelle(prime_annuelle)

    def _valider_prime_annuelle(self, prime_annuelle):
        while not (300000 <= prime_annuelle <= 600000): 
            print(f"Erreur: La prime annuelle {prime_annuelle} est invalide (doit être entre 300000 et 600000 MAD).")
            prime_annuelle = float(input("Veuillez entrer une prime valide: "))
        return prime_annuelle

    @property
    def nom(self):
        return self._nom

    @property
    def date_fin_contrat(self):
        return self._date_fin_contrat

    @property
    def nb_annees_contrat(self):
        return self._nb_annees_contrat

    @property
    def prime_annuelle(self):
        return self._prime_annuelle

    def DeterminerDebutContrat(self):
        date_fin = datetime.strptime(self.date_fin_contrat, "%Y-%m-%d")
        debut_contrat = datetime(date_fin.year - self.nb_annees_contrat, date_fin.month, date_fin.day)
        return debut_contrat.strftime("%Y-%m-%d")

    def __str__(self):
        return (f"Entraîneur: {self.nom}, Date fin contrat: {self.date_fin_contrat}, "
                f"Années contrat: {self.nb_annees_contrat}, Prime: {self.prime_annuelle} MAD")



class Selection:
    def __init__(self, pays, surnom, matchs_internes, matchs_externes, entraineur):
        self._pays = pays
        self._surnom = surnom
        self._matchs_internes = matchs_internes
        self._matchs_externes = matchs_externes
        self._joueurs = []
        self._entraineur = entraineur

    @property
    def pays(self):
        return self._pays

    @property
    def surnom(self):
        return self._surnom

    @property
    def matchs_internes(self):
        return self._matchs_internes

    @property
    def matchs_externes(self):
        return self._matchs_externes

    @property
    def entraineur(self):
        return self._entraineur

    def AjouterJoueur(self, joueur):
        self._joueurs.append(joueur)
        print(f"Joueur {joueur.nom} ajouté à la sélection.")

    def SupprimerJoueur(self, nom):
        for joueur in self._joueurs:
            if joueur.nom == nom:
                self._joueurs.remove(joueur)
                print(f"Joueur {nom} supprimé de la sélection.")
                return
        print(f"Aucun joueur trouvé avec le nom {nom}.")

    def NombreJoueurInternationaux(self):
        return sum(1 for joueur in self._joueurs if isinstance(joueur, International))

    def AfficherSelection(self):
        print(f"\nSélection nationale: {self.pays} ({self.surnom})\n")
        print(f"Entraîneur: {self.entraineur}\n")
        print("Liste des joueurs:")
        for joueur in self._joueurs:
            print(joueur)

    def __str__(self):
        return f"Sélection: {self.pays} ({self.surnom}), Matchs internes: {self.matchs_internes}, Matchs externes: {self.matchs_externes}"

if __name__ == "__main__":
    entraineur = Entraineur("Zinedine Zidane", "2026-12-31", 4, 700000)
    
    selection = Selection("Maroc", "Lions de l'Atlas", 10, 5, entraineur)

    joueur1 = Joueur("Achraf Hakimi", 24, "Défenseur", True)
    joueur2 = International("Hakim Ziyech", 30, "Milieu", True, 35)  
    joueur3 = Joueur("Yassine Bounou", 32, "Gardien", False)

    selection.AjouterJoueur(joueur1)
    selection.AjouterJoueur(joueur2)
    selection.AjouterJoueur(joueur3)

    selection.AfficherSelection()

    print(f"\nNombre de joueurs internationaux: {selection.NombreJoueurInternationaux()}")

    selection.SupprimerJoueur("Achraf Hakimi")

    selection.AfficherSelection()

    print(f"\nPrime de {joueur2.nom}: {joueur2.CalculerPrime(selection.matchs_internes, selection.matchs_externes)} MAD")

    print(f"Début du contrat de l'entraîneur: {entraineur.DeterminerDebutContrat()}")