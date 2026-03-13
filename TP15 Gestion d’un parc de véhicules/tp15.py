from abc import ABC, abstractmethod

class Vehicule(ABC):
    def __init__(self, immatriculation, date_acquisition, etat, prix_achat):
        self.immatriculation = immatriculation
        self.date_acquisition = date_acquisition
        self.etat = etat  # "opérationnel" ou "non opérationnel"
        self.prix_achat = prix_achat

    @abstractmethod
    def __str__(self):
        pass


class Voiture(Vehicule):
    def __init__(self, immatriculation, date_acquisition, etat, prix_achat, marque, modele, couleur):
        super().__init__(immatriculation, date_acquisition, etat, prix_achat)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur

    def __str__(self):
        return (f"Voiture [Immatriculation: {self.immatriculation}, Date d'acquisition: {self.date_acquisition}, "
                f"État: {self.etat}, Prix: {self.prix_achat} €, Marque: {self.marque}, "
                f"Modèle: {self.modele}, Couleur: {self.couleur}]")


class Camion(Vehicule):
    def __init__(self, immatriculation, date_acquisition, etat, prix_achat, capacite_charge, type_cargaison):
        super().__init__(immatriculation, date_acquisition, etat, prix_achat)
        self.capacite_charge = capacite_charge
        self.type_cargaison = type_cargaison

    def __str__(self):
        return (f"Camion [Immatriculation: {self.immatriculation}, Date d'acquisition: {self.date_acquisition}, "
                f"État: {self.etat}, Prix: {self.prix_achat} €, Capacité: {self.capacite_charge} tonnes, "
                f"Type de cargaison: {self.type_cargaison}]")


class Moto(Vehicule):
    def __init__(self, immatriculation, date_acquisition, etat, prix_achat, cylindree, type_moto):
        super().__init__(immatriculation, date_acquisition, etat, prix_achat)
        self.cylindree = cylindree
        self.type_moto = type_moto

    def __str__(self):
        return (f"Moto [Immatriculation: {self.immatriculation}, Date d'acquisition: {self.date_acquisition}, "
                f"État: {self.etat}, Prix: {self.prix_achat} €, Cylindrée: {self.cylindree} cm³, "
                f"Type: {self.type_moto}]")


class Garage:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.vehicules = []

    def __str__(self):
        return f"Garage [Nom: {self.nom}, Adresse: {self.adresse}, Nombre de véhicules: {len(self.vehicules)}]"

    def ajouterVehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def rechercheVehicule(self, immatriculation):
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                return vehicule
        return None

    def supprimerVehicule(self, immatriculation):
        vehicule = self.rechercheVehicule(immatriculation)
        if vehicule:
            self.vehicules.remove(vehicule)
            return True
        return False


class CompagnieTransport:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.garages = []

    def __str__(self):
        return f"Compagnie [Nom: {self.nom}, Adresse: {self.adresse}, Nombre de garages: {len(self.garages)}]"

    def ajouterGarage(self, garage):
        self.garages.append(garage)

    def transfertVehicule(self, immatriculation, garage_source, garage_destination):
        vehicule = garage_source.rechercheVehicule(immatriculation)
        if vehicule:
            garage_source.supprimerVehicule(immatriculation)
            garage_destination.ajouterVehicule(vehicule)
            return True
        return False

    def exporterDonnees(self, nom_fichier):
        with open(nom_fichier, "w") as fichier:
            fichier.write(f"Compagnie : {self.nom}\nAdresse : {self.adresse}\n\n")
            for garage in self.garages:
                fichier.write(str(garage) + "\n")
                for vehicule in garage.vehicules:
                    fichier.write(f"  {vehicule}\n")
        return True



if __name__ == "__main__":
    compagnie = CompagnieTransport("Transport Global", "45 Avenue Centrale")

    garage_nord = Garage("Garage Nord", "1 Rue des Lilas")
    garage_sud = Garage("Garage Sud", "5 Boulevard de l'Espoir")

    compagnie.ajouterGarage(garage_nord)
    compagnie.ajouterGarage(garage_sud)

    voiture = Voiture("AB-123-CD", "2022-01-15", "opérationnel", 15000, "Toyota", "Yaris", "Rouge")
    camion = Camion("XY-987-ZT", "2021-06-10", "opérationnel", 30000, 10, "Livraisons")
    moto = Moto("MT-456-UV", "2020-03-20", "non opérationnel", 8000, 600, "Cross")

    garage_nord.ajouterVehicule(voiture)
    garage_sud.ajouterVehicule(camion)
    garage_nord.ajouterVehicule(moto)

    print(compagnie)
    for garage in compagnie.garages:
        print(garage)
        for vehicule in garage.vehicules:
            print(f"  {vehicule}")

    compagnie.transfertVehicule("MT-456-UV", garage_nord, garage_sud)

    compagnie.exporterDonnees("donnees_transport.txt")
    print("\nDonnées exportées dans 'donnees_transport.txt'")
