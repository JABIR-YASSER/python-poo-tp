class Chauffeur:
    def __init__(self, cin, nom, prenom):
        self._cin = cin
        self._nom = nom
        self._prenom = prenom

    @property
    def cin(self):
        return self._cin

    @cin.setter
    def cin(self, value):
        self._cin = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    def __str__(self):
        return f"Chauffeur: {self.nom} {self.prenom}, CIN: {self.cin}"


class Bus:
    def __init__(self, immatriculation, marque, type_bus):
        self._immatriculation = immatriculation
        self._marque = marque
        self._type_bus = type_bus

    @property
    def immatriculation(self):
        return self._immatriculation

    @immatriculation.setter
    def immatriculation(self, value):
        self._immatriculation = value

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        self._marque = value

    @property
    def type_bus(self):
        return self._type_bus

    @type_bus.setter
    def type_bus(self, value):
        self._type_bus = value

    def __str__(self):
        return f"Bus: {self.marque}, Immatriculation: {self.immatriculation}, Type: {self.type_bus}"


class Voyage:
    numero_voyage_counter = 1

    def __init__(self, vchauffeur, vbus, date_voyage, ville_depart, ville_arrivee, nb_voyageurs, prix_billet):
        self._numero_voyage = Voyage.numero_voyage_counter
        Voyage.numero_voyage_counter += 1
        self._vchauffeur = vchauffeur
        self._vbus = vbus
        self._date_voyage = date_voyage
        self._ville_depart = ville_depart
        self._ville_arrivee = ville_arrivee
        self._nb_voyageurs = nb_voyageurs
        self._prix_billet = prix_billet

    @property
    def numero_voyage(self):
        return self._numero_voyage

    @property
    def vchauffeur(self):
        return self._vchauffeur

    @vchauffeur.setter
    def vchauffeur(self, value):
        self._vchauffeur = value

    @property
    def vbus(self):
        return self._vbus

    @vbus.setter
    def vbus(self, value):
        self._vbus = value

    @property
    def date_voyage(self):
        return self._date_voyage

    @date_voyage.setter
    def date_voyage(self, value):
        self._date_voyage = value

    @property
    def ville_depart(self):
        return self._ville_depart

    @ville_depart.setter
    def ville_depart(self, value):
        self._ville_depart = value

    @property
    def ville_arrivee(self):
        return self._ville_arrivee

    @ville_arrivee.setter
    def ville_arrivee(self, value):
        self._ville_arrivee = value

    @property
    def nb_voyageurs(self):
        return self._nb_voyageurs

    @nb_voyageurs.setter
    def nb_voyageurs(self, value):
        self._nb_voyageurs = value

    @property
    def prix_billet(self):
        return self._prix_billet

    @prix_billet.setter
    def prix_billet(self, value):
        self._prix_billet = value

    @property
    def recette(self):
        return self._nb_voyageurs * self._prix_billet

    def __str__(self):
        return (f"Voyage {self.numero_voyage} - Date: {self.date_voyage}\n"
                f"Chauffeur: {self.vchauffeur.nom} {self.vchauffeur.prenom}\n"
                f"Bus: {self.vbus.immatriculation}, Marque: {self.vbus.marque}\n"
                f"De {self.ville_depart} à {self.ville_arrivee}\n"
                f"Recette: {self.recette}€")


class GestionVoyage:
    def __init__(self):
        self._chauffeurs = []
        self._bus = []
        self._voyages = []

    def ajouter_chauffeur(self, chauffeur):
        if any(c.cin == chauffeur.cin for c in self._chauffeurs):
            print("Chauffeur avec ce CIN existe déjà.")
        else:
            self._chauffeurs.append(chauffeur)
            print("Chauffeur ajouté.")

    def ajouter_bus(self, bus):
        if any(b.immatriculation == bus.immatriculation for b in self._bus):
            print("Bus avec cette immatriculation existe déjà.")
        else:
            self._bus.append(bus)
            print("Bus ajouté.")

    def ajouter_voyage(self, date_voyage, ville_depart, ville_arrivee, nb_voyageurs, prix_billet):
        cin_chauffeur = input("CIN du chauffeur: ")
        chauffeur = self.rechercher_chauffeur(cin_chauffeur)
        while not chauffeur:
            print("Chauffeur non trouvé, veuillez saisir un autre CIN.")
            cin_chauffeur = input("CIN du chauffeur: ")
            chauffeur = self.rechercher_chauffeur(cin_chauffeur)

        immatriculation_bus = input("Immatriculation du bus: ")
        bus = self.rechercher_bus(immatriculation_bus)
        while not bus:
            print("Bus non trouvé, veuillez saisir une autre immatriculation.")
            immatriculation_bus = input("Immatriculation du bus: ")
            bus = self.rechercher_bus(immatriculation_bus)

        voyage = Voyage(chauffeur, bus, date_voyage, ville_depart, ville_arrivee, nb_voyageurs, prix_billet)
        self._voyages.append(voyage)
        print("Voyage ajouté.")

    def rechercher_chauffeur(self, cin):
        for chauffeur in self._chauffeurs:
            if chauffeur.cin == cin:
                return chauffeur
        return None

    def rechercher_bus(self, immatriculation):
        for bus in self._bus:
            if bus.immatriculation == immatriculation:
                return bus
        return None

    def afficher_voyages(self):
        for voyage in self._voyages:
            print(voyage)


if __name__ == "__main__":
    gestion = GestionVoyage()
    while True:
        print("\nMenu:")
        print("1. Ajouter un chauffeur")
        print("2. Ajouter un bus")
        print("3. Ajouter un voyage")
        print("4. Afficher tous les voyages")
        print("5. Quitter")
        choix = input("Choisissez une option: ")

        if choix == "1":
            cin = input("CIN du chauffeur: ")
            nom = input("Nom du chauffeur: ")
            prenom = input("Prénom du chauffeur: ")
            chauffeur = Chauffeur(cin, nom, prenom)
            gestion.ajouter_chauffeur(chauffeur)

        elif choix == "2":
            immatriculation = input("Immatriculation du bus: ")
            marque = input("Marque du bus: ")
            type_bus = input("Type du bus: ")
            bus = Bus(immatriculation, marque, type_bus)
            gestion.ajouter_bus(bus)

        elif choix == "3":
            date_voyage = input("Date du voyage: ")
            ville_depart = input("Ville de départ: ")
            ville_arrivee = input("Ville d'arrivée: ")
            nb_voyageurs = int(input("Nombre de voyageurs: "))
            prix_billet = float(input("Prix du billet: "))
            gestion.ajouter_voyage(date_voyage, ville_depart, ville_arrivee, nb_voyageurs, prix_billet)

        elif choix == "4":
            gestion.afficher_voyages()

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")