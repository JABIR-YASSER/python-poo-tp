class Etudiant:
    def __init__(self, matricule, nom, programme_d_etudes):
        self.matricule = matricule
        self.nom = nom
        self.programme_d_etudes = programme_d_etudes
        self.notes = []

    def ajouter_note(self, note):
        self.notes.append(note)

    def calculer_moyenne(self):
        return sum(self.notes) / len(self.notes) if self.notes else 0

    def __str__(self):
        moyenne = self.calculer_moyenne()
        return f"Matricule: {self.matricule}\nNom: {self.nom}\nProgramme d'études: {self.programme_d_etudes}\nMoyenne: {moyenne:.2f}"

liste_etudiants = []
nombre = int(input("Donner le nombre d'étudiants : "))

for i in range(nombre):
    matricule = input("Donner le matricule de l'étudiant : ")
    nom = input("Donner le nom de l'étudiant : ")
    programme_d_etudes = input("Donner le programme d'études de l'étudiant : ")
    etudiant = Etudiant(matricule, nom, programme_d_etudes)

    nbr_notes = int(input(f"Combien de notes pour l'étudiant {nom} ? "))
    for n in range(nbr_notes):
        note = float(input(f"Entrer la note {n+1} : "))
        etudiant.ajouter_note(note)

    liste_etudiants.append(etudiant)

for etudiant in liste_etudiants:
    print(etudiant)
