from abc import ABC, abstractmethod


class Vehicule(ABC):
    def __init__(self, immatriculation, date_achat, etat, prix_achat):
        self.immatriculation = immatriculation
        self.date_achat = date_achat
        self.etat = etat
        self.prix_achat = prix_achat

    @abstractmethod
    def __str__(self):
        pass  



class Voiture(Vehicule):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, marque, modele, couleur):
        super().__init__(immatriculation, date_achat, etat, prix_achat)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur

    def __str__(self):
        return (f"Immatriculation: {self.immatriculation}, Date d'achat: {self.date_achat}, "
                f"État: {self.etat}, Prix d'achat: {self.prix_achat} €, "
                f"Marque: {self.marque}, Modèle: {self.modele}, Couleur: {self.couleur}")


class Camion(Vehicule):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, capacite_charge, dimensions):
        super().__init__(immatriculation, date_achat, etat, prix_achat)
        self.capacite_charge = capacite_charge 
        self.dimensions = dimensions 

    def __str__(self):
        return (f"Immatriculation: {self.immatriculation}, Date d'achat: {self.date_achat}, "
                f"État: {self.etat}, Prix d'achat: {self.prix_achat} €, "
                f"Capacité de charge: {self.capacite_charge} tonnes, "
                f"Dimensions: {self.dimensions[0]}m x {self.dimensions[1]}m x {self.dimensions[2]}m")


class VehiculeHybride(Camion,Voiture):
    def __init__(self, immatriculation, date_achat, etat, prix_achat, marque, modele, couleur,
                 capacite_charge, dimensions):
        
        self.voiture = Voiture(immatriculation, date_achat, etat, prix_achat, marque, modele, couleur)
        self.camion = Camion(immatriculation, date_achat, etat, prix_achat, capacite_charge, dimensions)

    def __str__(self):
        return (f"{self.voiture}, "  
                f"Capacité de charge: {self.camion.capacite_charge} tonnes, "
                f"Dimensions: {self.camion.dimensions[0]}m x {self.camion.dimensions[1]}m x {self.camion.dimensions[2]}m")

    def prix_achat(self):
        return self.voiture.prix_achat  


class Agence:
    def __init__(self, code, adresse):
        self.code = code
        self.adresse = adresse
        self.vehicules = []

    def __str__(self):
        return (f"Agence Code: {self.code}, Adresse: {self.adresse}, "
                f"Nombre de véhicules: {len(self.vehicules)}")

    def ajouterVehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def rechercheVehicule(self, immatriculation):
        for vehicule in self.vehicules:
            if vehicule.immatriculation == immatriculation:
                return vehicule
        return None 

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
            print(f"Véhicule {immatriculation} supprimé de la flotte.")
            return True
        print(f"Erreur : Véhicule {immatriculation} introuvable.")
        return False

    def modifierEtatVehicule(self, immatriculation, nouvel_etat):
        vehicule = self.rechercheVehicule(immatriculation)
        if vehicule:
            if nouvel_etat in ["disponible", "en maintenance", "loué"]:
                vehicule.etat = nouvel_etat
                print(f"L'état du véhicule {immatriculation} a été mis à jour à '{nouvel_etat}'.")
                return True
            print("Erreur : L'état doit être 'disponible', 'en maintenance' ou 'loué'.")
            return False
        print(f"Erreur : Véhicule {immatriculation} introuvable.")
        return False

    def totalValeurFlotte(self):
        total = 0
        for vehicule in self.vehicules:
            if isinstance(vehicule, VehiculeHybride):
                total += vehicule.voiture.prix_achat  
            else:
                total += vehicule.prix_achat
        return total



agence = Agence("A1", "123 Rue Principale")


voiture = Voiture("AB-123-CD", "2023-01-15", "disponible", 20000, "Toyota", "Corolla", "Rouge")
camion = Camion("XY-987-ZT", "2022-06-10", "en maintenance", 50000, 10, (6, 2.5, 3))
hybride = VehiculeHybride("HY-456-UV", "2021-03-20", "loué", 30000, "Tesla", "Model X", "Noir", 8, (5, 2, 2.5))

agence.ajouterVehicule(voiture)
agence.ajouterVehicule(camion)
agence.ajouterVehicule(hybride)

print(agence)
agence.inventaire()

print(f"Valeur totale de la flotte : {agence.totalValeurFlotte()} €")
