class Employe:
    def __init__(self, ID, nom, prenom):
        self.__ID = ID
        self.__nom = nom
        self.__prenom = prenom
    
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
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    def __str__(self):
        return f"ID: {self.ID}\nNom: {self.nom}\nPrenom: {self.prenom}"

class Salle:
    def __init__(self, num, nom, capacite):
        self.__num = num
        self.__nom = nom
        self.__capacite = capacite
    
    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, value):
        self.__num = value
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, value):
        self.__nom = value
    
    @property
    def capacite(self):
        return self.__capacite
    
    @capacite.setter
    def capacite(self, value):
        self.__capacite = value
        
    def __str__(self):
        return f"Numéro: {self.num}\nNom: {self.nom}\nCapacité: {self.capacite}"

class Reservation:
    c = 0
    def __init__(self, employe, salle, date_heure_debut, date_heure_fin, objectif):
        Reservation.c += 1
        self.__numero_reservation = Reservation.c
        self.__employe = employe
        self.__salle = salle
        self.__date_heure_debut = date_heure_debut
        self.__date_heure_fin = date_heure_fin
        self.__objectif = objectif
    
    @property
    def numero_reservation(self):
        return self.__numero_reservation
    
    @numero_reservation.setter
    def numero_reservation(self, value):
        self.__numero_reservation = value
    
    @property
    def employe(self):
        return self.__employe
    
    @employe.setter
    def employe(self, value):
        self.__employe = value
    
    @property
    def salle(self):
        return self.__salle
    
    @salle.setter
    def salle(self, value):
        self.__salle = value
    
    @property
    def date_heure_debut(self):
        return self.__date_heure_debut
    
    @date_heure_debut.setter
    def date_heure_debut(self, value):
        self.__date_heure_debut = value
    
    @property
    def date_heure_fin(self):
        return self.__date_heure_fin
    
    @date_heure_fin.setter
    def date_heure_fin(self, value):
        self.__date_heure_fin = value
    
    @property
    def objectif(self):
        return self.__objectif
    
    @objectif.setter
    def objectif(self, value):
        self.__objectif = value
    
    def __str__(self):
        return f"Numéro de réservation: {self.numero_reservation}\nEmployé: {self.employe}\nSalle: {self.salle}\nDate et heure de début: {self.date_heure_debut}\nDate et heure de fin: {self.date_heure_fin}\nObjectif: {self.objectif}" 

class GestionReservations:
    def __init__(self):
        self.employes = []
        self.salles = []
        self.reservations = []
    
    def ajouter_employe(self, employe):
        if not any(emp.ID == employe.ID for emp in self.employes):
            self.employes.append(employe)
    
    def ajouter_salle(self, salle):
        if not any(sal.num == salle.num for sal in self.salles):
            self.salles.append(salle)
    
    def ajouter_reservation(self):
        employe_id = int(input("Saisir l'ID de l'employé pour la réservation : "))
        employe = self.chercher_employe(employe_id)
        while employe is None:
            print("Aucun employé trouvé avec cet ID. Veuillez saisir un autre ID.")
            employe_id = int(input("Saisir l'ID de l'employé pour la réservation : "))
            employe = self.chercher_employe(employe_id)
        salle_num = int(input("Saisir le numéro de la salle pour la réservation : "))
        salle = self.chercher_salle(salle_num)
        while salle is None:
            print("Aucune salle trouvée avec ce numéro. Veuillez saisir un autre numéro.")
            salle_num = int(input("Saisir le numéro de la salle pour la réservation : "))
            salle = self.chercher_salle(salle_num)
        date_heure_debut = input("Saisir la date et l'heure de début de la réservation : ")
        date_heure_fin = input("Saisir la date et l'heure de fin de la réservation : ")
        objectif = input("Saisir l'objectif de la réservation : ")
        
        reservation = Reservation(employe, salle, date_heure_debut, date_heure_fin, objectif)
        self.reservations.append(reservation)
    
    def chercher_employe(self, ID):
        for employe in self.employes:
            if employe.ID == ID:
                return employe
        return None
    
    def chercher_salle(self, num):
        for salle in self.salles:
            if salle.num == num:
                return salle
        return None
    
    def chercher_reservation(self, num):
        for res in self.reservations:
            if res.numero_reservation == num:
                return res
        return None
    
    def afficher_reservations(self):
        for reservation in self.reservations:
            print(reservation)

if __name__ == "__main__":
    gestion_reservations = GestionReservations()

    while True:
        print("\nMenu:")
        print("1. Ajouter un employé")
        print("2. Ajouter une salle")
        print("3. Ajouter une réservation")
        print("4. Chercher un employé")
        print("5. Chercher une salle")
        print("6. Afficher les réservations")
        print("7. Quitter")

        choix = input("Veuillez choisir une option (1-7): ")

        if choix == '1':
            id_employe = int(input("Entrez l'ID de l'employé: "))
            nom = input("Entrez le nom de l'employé: ")
            prenom = input("Entrez le prénom de l'employé: ")
            employe = Employe(id_employe, nom, prenom)
            gestion_reservations.ajouter_employe(employe)
            print("Employé ajouté avec succès.")

        elif choix == '2':
            num_salle = int(input("Entrez le numéro de la salle: "))
            nom_salle = input("Entrez le nom de la salle: ")
            capacite = int(input("Entrez la capacité de la salle: "))
            salle = Salle(num_salle, nom_salle, capacite)
            gestion_reservations.ajouter_salle(salle)
            print("Salle ajoutée avec succès.")

        elif choix == '3':
            gestion_reservations.ajouter_reservation()
            print("Réservation ajoutée avec succès.")

        elif choix == '4':
            id_employe = int(input("Entrez l'ID de l'employé à chercher: "))
            employe = gestion_reservations.chercher_employe(id_employe)
            if employe:
                print("Employé trouvé:")
                print(employe)
            else:
                print("Aucun employé trouvé avec cet ID.")

        elif choix == '5':
            num_salle = int(input("Entrez le numéro de la salle à chercher: "))
            salle = gestion_reservations.chercher_salle(num_salle)
            if salle:
                print("Salle trouvée:")
                print(salle)
            else:
                print("Aucune salle trouvée avec ce numéro.")

        elif choix == '6':
            print("Affichage des réservations:")
            gestion_reservations.afficher_reservations()

        elif choix == '7':
            print("Au revoir!")
            break

        else:
            print("Choix invalide, veuillez réessayer.")