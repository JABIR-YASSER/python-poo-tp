from datetime import datetime

class Employe:
    compteur_matricule = 0  

    def __init__(self, nom, prenom):
        Employe.compteur_matricule += 1
        self.matricule = Employe.compteur_matricule
        self._nom = nom
        self._prenom = prenom
        self.date_embauche = datetime.now()
        self.solde_conges = None 
    
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
        return (f"Matricule: {self.matricule}, Nom: {self.nom}, Prénom: {self.prenom}, "
                f"Date d'embauche: {self.date_embauche.strftime('%Y-%m-%d')}")

class Manager(Employe):
    def __init__(self, nom, prenom, code_manager):
        super().__init__(nom, prenom)
        self._code_manager = code_manager
        self.liste_employes = []
    
    @property
    def code_manager(self):
        return self._code_manager

    @code_manager.setter
    def code_manager(self, value):
        self._code_manager = value

    def __str__(self):
        return (f"{super().__str__()}, Code Manager: {self.code_manager}, "
                f"Nombre d'employés: {len(self.liste_employes)}")

    def listeEmployes(self):
        return [employe.nom for employe in self.liste_employes]

    def ajouterEmploye(self, employe):
        self.liste_employes.append(employe)

    def getEmployeByCode(self, matricule):
        for employe in self.liste_employes:
            if employe.matricule == matricule:
                return employe
        return None

    def trierEmployes(self):
        self.liste_employes.sort(key=lambda emp: emp.nom)

class DemandeConge:
    def __init__(self, code_employe, date_debut, duree, motif):
        self._code_employe = code_employe
        self._date_debut = date_debut
        self._duree = duree
        self._motif = motif
        self._etat = "En cours"

    @property
    def code_employe(self):
        return self._code_employe

    @code_employe.setter
    def code_employe(self, value):
        self._code_employe= value
    
    @property
    def date_debut(self):
        return self._date_debut

    @date_debut.setter
    def date_debut(self, value):
        self._date_debut = value
    
    @property
    def duree(self):
        return self._duree

    @duree.setter
    def duree(self, value):
        self._duree = value
    
    @property
    def motif(self):
        return self._motif

    @motif.setter
    def motif(self, value):
        self._motif= value
    
    def valider(self):
        self.etat = "Validé"

    def refuser(self):
        self.etat = "Refusé"

    def __str__(self):
        return (f"Code Employé: {self.code_employe}, Date Début: {self.date_debut}, "
                f"Durée: {self.duree} jours, Motif: {self.motif}, État: {self.etat}")

class GestionConge:
    def __init__(self):
        self.liste_managers = []
        self.liste_demandes = []

    def ajouterDemandeConge(self, demande):
        self.liste_demandes.append(demande)
    
    def listeDemandeCongeEnCours(self):
        return [demande for demande in self.liste_demandes if demande.etat == "En cours"]

    def listeDemandeCongeParEmploye(self, code_employe):
        return [demande for demande in self.liste_demandes if demande.code_employe == code_employe]
    
    def listeDemandeCongeParManager(self, code_manager):
        for manager in self.liste_managers:
            if manager.code_manager == code_manager:
                return [demande for demande in self.liste_demandes
                        if demande.code_employe in [emp.matricule for emp in manager.liste_employes]]
        return []

    def dureeTotalConge(self):
        total_conge = {}
        for demande in self.liste_demandes:
            if demande.etat == "Validé":
                total_conge[demande.code_employe] = total_conge.get(demande.code_employe, 0) + demande.duree
        return total_conge


emp1 = Employe("Dupont", "Jean")
emp2 = Employe("Durand", "Claire")
manager = Manager("Martin", "Paul", "M001")

manager.ajouterEmploye(emp1)
manager.ajouterEmploye(emp2)

print(manager.listeEmployes())

employe_recherche = manager.getEmployeByCode(emp1.matricule)
print("\nRecherche d'un employé par matricule :")
print(employe_recherche)

gestion = GestionConge()
gestion.liste_managers.append(manager)

demande1 = DemandeConge(emp1.matricule, "2024-12-01", 5, "Vacances")
demande2 = DemandeConge(emp2.matricule, "2024-12-10", 3, "Formation")

gestion.ajouterDemandeConge(demande1)
gestion.ajouterDemandeConge(demande2)

demande1.valider()
demande2.refuser()

for demande in gestion.listeDemandeCongeEnCours():
    print(demande)

for demande in gestion.listeDemandeCongeParManager(manager.code_manager):
    print(demande)

total_conges = gestion.dureeTotalConge()
for code_employe, duree in total_conges.items():
    print(f"Code Employé: {code_employe}, Durée totale: {duree} jours")