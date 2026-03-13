class Adress:
    def __init__ (self,rue,ville):
        self.rue=rue
        self.ville=ville
    def afficher (self):
        print(f"rue:{self.rue}\nville:{self.ville}")
    def __str__(self):
        return (f"rue:{self.rue}\nville:{self.ville}")

class Personne :
    def __init__(self,code,nom,adress):
        self.code=code
        self.nom=nom
        self.adress=adress
    def affiche (self):
        print(f"code:{self.code}\nnom:{self.nom}")
        self.adress.afficher()
    def __str__(self):
        ad=self.adress.__str__()
        return (f"code:{self.code}\nnom:{self.nom}\nadress:{ad}")
a=Adress("v1","r1")
p=Personne(1,"n2",a)
p.affiche()
print("----------------------------")
print(p)
    
    