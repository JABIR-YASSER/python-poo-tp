class Patient:
    def __init__(self, numero_dossier, nom, prenom, date_naissance, sexe, adresse, num_secu):
        self.numero_dossier = numero_dossier
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.adresse = adresse
        self.num_secu = num_secu

    def __str__(self):
        return f"Patient {self.nom} {self.prenom} (Dossier: {self.numero_dossier})"


class Medecin:
    def __init__(self, numero_id, nom, prenom, specialite):
        self.numero_id = numero_id
        self.nom = nom
        self.prenom = prenom
        self.specialite = specialite

    def __str__(self):
        return f"Dr. {self.nom} {self.prenom} (Spécialité: {self.specialite})"


class RendezVous:
    num_rdv_counter = 1

    def __init__(self, patient, medecin, date_heure, motif):
        self.num_rdv = RendezVous.num_rdv_counter
        RendezVous.num_rdv_counter += 1
        self.patient = patient
        self.medecin = medecin
        self.date_heure = date_heure
        self.motif = motif

    def __str__(self):
        return f"Rendez-vous #{self.num_rdv} avec {self.medecin} pour {self.patient} le {self.date_heure} - Motif: {self.motif}"


class Traitement:
    num_traitement_counter = 1

    def __init__(self, patient, description, date_debut, date_fin):
        self.num_traitement = Traitement.num_traitement_counter
        Traitement.num_traitement_counter += 1
        self.patient = patient
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin

    def __str__(self):
        return f"Traitement #{self.num_traitement} pour {self.patient}: {self.description} ({self.date_debut} - {self.date_fin})"


class GestionClinique:
    def __init__(self):
        self.patients = []
        self.medecins = []
        self.rendez_vous = []
        self.traitements = []

    def ajouter_patient(self, patient):
        self.patients.append(patient)

    def ajouter_medecin(self, medecin):
        self.medecins.append(medecin)

    def prendre_rendez_vous(self, patient, medecin, date_heure, motif):
        rdv = RendezVous(patient, medecin, date_heure, motif)
        self.rendez_vous.append(rdv)
        return rdv

    def prescrire_traitement(self, patient, description, date_debut, date_fin):
        traitement = Traitement(patient, description, date_debut, date_fin)
        self.traitements.append(traitement)
        return traitement

    def annuler_rendez_vous(self, num_rdv):
        self.rendez_vous = [rdv for rdv in self.rendez_vous if rdv.num_rdv != num_rdv]

    def modifier_rendez_vous(self, num_rdv, new_date_heure):
        for rdv in self.rendez_vous:
            if rdv.num_rdv == num_rdv:
                rdv.date_heure = new_date_heure
                return rdv
        return None

    def lister_rendez_vous_par_patient(self, patient):
        return [rdv for rdv in self.rendez_vous if rdv.patient == patient]

    def lister_traitements_par_patient(self, patient):
        return [traitement for traitement in self.traitements if traitement.patient == patient]

    def afficher_agenda_medecin(self, medecin):
        return [rdv for rdv in self.rendez_vous if rdv.medecin == medecin]
