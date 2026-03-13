from abc import ABC, abstractmethod


class Equipement(ABC):
    def __init__(self, code, date_acquisition, etat, prix_achat):
        self.code = code
        self.date_acquisition = date_acquisition
        self.etat = etat
        self.prix_achat = prix_achat

    @abstractmethod
    def __str__(self):
        return (f"Code: {self.code}, Date d'acquisition: {self.date_acquisition}, "
                f"État: {'Opérationnel' if self.etat else 'Non opérationnel'}, Prix: {self.prix_achat} €")


class Ordinateur(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, marque, taille_ecran):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.marque = marque
        self.taille_ecran = taille_ecran

    def __str__(self):
        eq=super().__str__()
        return (eq +f" , Marque: {self.marque}, Taille écran: {self.taille_ecran} pouces")


class Table(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, longueur, largeur):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.longueur = longueur
        self.largeur = largeur
    def __str__(self):
        eq=super().__str__()
        return ( eq + f" , Longueur: {self.longueur} m, Largeur: {self.largeur} m")


class Chaise(Equipement):
    def __init__(self, code, date_acquisition, etat, prix_achat, couleur):
        super().__init__(code, date_acquisition, etat, prix_achat)
        self.couleur = couleur

    def __str__(self):
        eq=super().__str__()
        return eq + f", Couleur: {self.couleur}"


class Bureau:
    def __init__(self, code, description):
        self.code = code
        self.description = description
        self.equipements = []

    def __str__(self):
        return (f"Bureau Code: {self.code}, Description: {self.description}, "
                f"Nombre d'équipements: {len(self.equipements)}")

    def ajouterEquipement(self, equipement):
        self.equipements.append(equipement)

    def rechercheEquipement(self, code):
        for equipement in self.equipements:
            if equipement.code == code:
                return equipement
        return None 

    def ficheInventaire(self):
        print(f"Fiche d'inventaire du bureau {self.code} ({self.description}):")
        if not self.equipements:
            print("Aucun équipement dans ce bureau.")
        for equipement in self.equipements:
            print(equipement)

    def supprimerEquipement(self, code):
        equipement = self.rechercheEquipement(code)
        if equipement:
            self.equipements.remove(equipement)
            return True
        return False


class Entreprise:
    def __init__(self, nom, adresse, telephone):
        self.nom = nom
        self.adresse = adresse
        self.telephone = telephone
        self.bureaux = []

    def __str__(self):
        return f"Entreprise: {self.nom}, Nombre de bureaux: {len(self.bureaux)}"

    def ajouterBureau(self, bureau):
        self.bureaux.append(bureau)

    def rechercheEquipement(self, code):
        for bureau in self.bureaux:
            equipement = bureau.rechercheEquipement(code)
            if equipement is not None:
                return equipement
        return None

    def localisation(self, code):
        for bureau in self.bureaux:
            equipement = bureau.rechercheEquipement(code)
            if equipement is not None:
                return f"L'équipement avec le code {code} se trouve dans le bureau : {bureau.description}"
        return f"L'équipement avec le code {code} n'est affecté à aucun bureau."

    def transferEquipement(self, code, bureau_source, bureau_destination):
        equipement = bureau_source.rechercheEquipement(code)
        if equipement:
            if bureau_source.supprimerEquipement(code):
                bureau_destination.ajouterEquipement(equipement)
                print(f"Équipement {code} transféré de {bureau_source.code} à {bureau_destination.code}.")
                return True
        print(f"Transfert échoué : équipement {code} introuvable dans le bureau {bureau_source.code}.")
        return False

    def exporter(self, fichier):
        with open(fichier, "w") as f:
            f.write(f"Entreprise: {self.nom}, Adresse: {self.adresse}, Téléphone: {self.telephone}\n")
            for bureau in self.bureaux:
                f.write(str(bureau) + "\n")
                for equipement in bureau.equipements:
                    f.write("  " + str(equipement) + "\n")
        print(f"Données exportées vers le fichier {fichier}.")


if __name__ == "__main__":
    ordinateur = Ordinateur("O123", "2023-01-15", True, 1500.0, "Dell", 15.6)
    table = Table("T456", "2022-06-10", False, 200.0, 1.5, 0.8)
    chaise = Chaise("C789", "2021-03-20", True, 50.0, "Rouge")

    bureau1 = Bureau("B1", "Bureau Administratif")
    bureau2 = Bureau("B2", "Salle de réunion")

    bureau1.ajouterEquipement(ordinateur)
    bureau1.ajouterEquipement(chaise)
    bureau2.ajouterEquipement(table)

    entreprise = Entreprise("TechCorp", "123 Rue Principale", "0123456789")
    entreprise.ajouterBureau(bureau1)
    entreprise.ajouterBureau(bureau2)

    print(entreprise)
    bureau1.ficheInventaire()
    bureau2.ficheInventaire()

    print(entreprise.localisation("O123"))
    entreprise.transferEquipement("O123", bureau1, bureau2)
    print(entreprise.localisation("O123"))

    entreprise.exporter("inventaire.txt")