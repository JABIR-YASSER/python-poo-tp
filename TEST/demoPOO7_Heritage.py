#classe mère
class Personne:
    def __init__(self,n,p):
        self.nom=n
        self.prenom=p
    def afficherInfos(self):
        print("nom:",self.nom,"prénom:",self.prenom)
    def __str__(self):
        return "---nom: "+self.nom+"\n---prénom: "+self.prenom
#classe fille
class Stagiaire(Personne):   
    def __init__(self,n,p,notes):
        #Personne.__init__(self,n,p)
        super().__init__(n,p)
        self.notes =notes
    def afficherNotes(self):
        print(self.notes)
    def afficherInfos(self):
        #print("nom:",self.nom,"prénom:",self.prenom)
        #print("notes:",self.notes)
        Personne.afficherInfos(self)
        self.afficherNotes()
    def __str__(self):
        res=super().__str__()
        return res+"\n---notes: "+str(self.notes)
        
stg=Stagiaire("n1","p1",10)
stg.afficherInfos()
#print(stg)
        
        
      
       


















