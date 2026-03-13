from abc import ABC, abstractmethod

# Classe abstraite pour les véhicules
class Vehicule(ABC):
    def __init__(self, immatriculation, date_achat, etat, prix_achat):
        self.immatriculation = immatriculation
        self.date_achat = date_achat
        self.etat = etat
        self.prix_achat = prix_achat

    @abstractmethod
    def __str__(self):
        return (f"Immatriculation: {self.immatriculation}, Date d'achat: {self.date_achat}, "
                f"État: {self.etat}, Prix d'achat: {self.prix_achat} dh")

# Classe Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, marque, modele, couleur):
        super().__init__(immatriculation, date_achat, etat, prix_achat)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur

    def __str__(self):
        return (super().__str__() +
                f", Marque: {self.marque}, Modèle: {self.modele}, Couleur: {self.couleur}")

class Camion(Vehicule):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, capacite_charge, dimensions):
        super().__init__(immatriculation, date_achat, etat, prix_achat)
        self.capacite_charge = capacite_charge
        self.dimensions = dimensions

    def __str__(self):
        return (super().__str__() +
                f", Capacité de charge: {self.capacite_charge} tonnes, "
                f"Dimensions: {self.dimensions[0]}m x {self.dimensions[1]}m x {self.dimensions[2]}m")

class Moto(Vehicule):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, cylindree, type_moto):
        super().__init__(immatriculation, date_achat, etat, prix_achat)
        self.cylindree = cylindree
        self.type_moto = type_moto

    def __str__(self):
        return (super().__str__() +
                f", Cylindrée: {self.cylindree} cm³, Type: {self.type_moto}")

class Agence:
    def __init__(self, code, adresse):
        self.code = code
        self.adresse = adresse
        self.vehicules = []

    def __str__(self):
        return (f"Agence Code: {self.code}, Adresse: {self.adresse}, "
                f"Nombre de véhicules: {len(self.vehicules)}")

    def rechercheVehicule(self, immatriculation):
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                return vehicule
        return None

    def ajouterVehicule(self, vehicule):
        if self.rechercheVehicule(vehicule.immatriculation):
            return f"Le véhicule avec immatriculation {vehicule.immatriculation} existe déjà."
        self.vehicules.append(vehicule)
        return f"Véhicule {vehicule.immatriculation} ajouté avec succès."

    def inventaire(self):
        print(f"Inventaire de l'agence {self.code} ({self.adresse}):")
        if not self.vehicules:
            print("Aucun véhicule dans l'agence.")
            return
        for vehicule in self.vehicules:
            print(vehicule)

    def supprimerVehicule(self, immatriculation):
        vehicule = self.rechercheVehicule(immatriculation)
        if vehicule:
            self.vehicules.remove(vehicule)
            print(f"Véhicule {immatriculation} supprimé de l'agence {self.code}.")
        else:
            print(f"Véhicule {immatriculation} introuvable dans l'agence {self.code}.")

class Entreprise:
    def __init__(self, nom):
        self.nom = nom
        self.agences = []

    def __str__(self):
        return f"Entreprise: {self.nom}, Nombre d'agences: {len(self.agences)}"

    def ajouterAgence(self, agence):
        if any(a.code == agence.code for a in self.agences):
            return "L'agence existe déjà."
        self.agences.append(agence)
        return "Agence ajoutée avec succès."

    def rechercheVehiculeGlobal(self, immatriculation):
        for agence in self.agences:
            vehicule = agence.rechercheVehicule(immatriculation)
            if vehicule:
                return vehicule
        raise Exception(f"Véhicule {immatriculation} introuvable dans toutes les agences.")

    def localisation(self, immatriculation):
        for agence in self.agences:
            vehicule = agence.rechercheVehicule(immatriculation)
            if vehicule:
                return agence
        raise Exception(f"Véhicule {immatriculation} introuvable dans toutes les agences.")

    def transfertVehicule(self, immatriculation, agence_source, agence_destination):
        vehicule = agence_source.rechercheVehicule(immatriculation)
        if vehicule:
            agence_source.supprimerVehicule(immatriculation)
            agence_destination.ajouterVehicule(vehicule)
            print(f"Véhicule {immatriculation} transféré de l'agence {agence_source.code} "
                  f"à l'agence {agence_destination.code}.")
        else:
            print(f"Véhicule {immatriculation} introuvable dans l'agence {agence_source.code}.")

    def exporter(self, fichier):
        with open(fichier, "w", encoding="utf-8") as f:
            f.write(f"Entreprise: {self.nom}\n")
            f.write(f"Nombre d'agences: {len(self.agences)}\n\n")
            for agence in self.agences:
                f.write(f"Agence Code: {agence.code}\n")
                f.write(f"Adresse: {agence.adresse}\n")
                f.write(f"Nombre de véhicules: {len(agence.vehicules)}\n")
                f.write("Liste des véhicules:\n")
                if agence.vehicules:
                    for vehicule in agence.vehicules:
                        f.write(f"  - {vehicule}\n")
                else:
                    f.write("  Aucun véhicule dans cette agence.\n")
                f.write("\n")
        print(f"Données exportées dans le fichier {fichier}.")

if __name__ == "__main__":
    voiture = Voiture("AB-123-CD", "2023-01-15", "disponible", 20000, "Toyota", "Corolla", "Rouge")
    camion = Camion("XY-987-ZT", "2022-06-10", "en maintenance", 50000, 10, (6, 2.5, 3))
    moto = Moto("MO-456-FG", "2021-03-20", "loué", 10000, 600, "sport")

    agence1 = Agence("A1", "123 Rue Principale")
    agence2 = Agence("A2", "456 Rue Secondaire")

    agence1.ajouterVehicule(voiture)
    agence1.ajouterVehicule(camion)
    agence2.ajouterVehicule(moto)

    entreprise = Entreprise("LocationCar")
    entreprise.ajouterAgence(agence1)
    entreprise.ajouterAgence(agence2)

    print(entreprise)
    agence1.inventaire()
    agence2.inventaire()

    try:
        vehicule = entreprise.rechercheVehiculeGlobal("MO-456-FG")
        print(f"Véhicule trouvé : {vehicule}")
    except Exception as e:
        print(e)

    entreprise.transfertVehicule("MO-456-FG", agence2, agence1)

    entreprise.exporter("flotte.txt")
