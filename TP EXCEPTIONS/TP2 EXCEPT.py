
class NoteInvalideError(Exception):
    def __init__(self, note):
        super().__init__(f"Note invalide : {note}. La note doit être entre 0 et 20.")

class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

    def ajouter_note(self, note):
        if 0 <= note <= 20:
            self.notes.append(note)
            print(f"Note {note} ajoutée pour {self.nom}.")
        else:
            raise NoteInvalideError(note)

    def moyenne(self):
        if not self.notes:
            return "Aucune note enregistrée."
        return sum(self.notes) / len(self.notes)


if __name__ == "__main__":
    etu = Etudiant("YASSER")

    notes_a_ajouter = [15, 18, 21, -6, 12]

    for note in notes_a_ajouter:
        try:
            etu.ajouter_note(note)
        except NoteInvalideError as e:
            print("Erreur :", e)

    print(f"Moyenne de {etu.nom} :", etu.moyenne())
