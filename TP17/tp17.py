from datetime import datetime

class Client:
    def __init__(self, code_client, nom, adresse="", tel="", email=""):
        self.code_client = code_client
        self.nom = nom
        self.adresse = adresse
        self.tel = tel
        self.email = email
    
    def __str__(self):
        return f"{self.nom} - {self.adresse}"

class Produit:
    def __init__(self, reference, designation, prix_unitaire, quantite_stock):
        self.reference = reference
        self.designation = designation
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock
    
    def __str__(self):
        return f"{self.reference} - {self.designation} - {self.prix_unitaire:.2f} EUR"

class Commande:
    compteur = 1000
    
    def __init__(self, client):
        Commande.compteur += 1
        self.num_commande = Commande.compteur
        self.client = client
        self.date_commande = datetime.now().strftime("%Y-%m-%d")
        self.produits = []
        self.quantites = []
    
    def __str__(self):
        return f"{self.num_commande}\t{self.date_commande}\t{self.client.nom}"
    
    def total_commande(self):
        return sum(p.prix_unitaire * q for p, q in zip(self.produits, self.quantites))
    
    def ajouter_produit(self, produit, quantite):
        if produit.quantite_stock >= quantite:
            self.produits.append(produit)
            self.quantites.append(quantite)
            produit.quantite_stock -= quantite
        else:
            print("Stock insuffisant!")
    
    def afficher_commande(self):
        print(f"Commande {self.num_commande} - Date : {self.date_commande} - Client : {self.client.nom}")
        print("Produits commandés:")
        for p, q in zip(self.produits, self.quantites):
            print(f"{p.designation} - {q} x {p.prix_unitaire:.2f} EUR = {q * p.prix_unitaire:.2f} EUR")
        print(f"Total: {self.total_commande():.2f} EUR\n")

clients = []
produits = []
commandes = []

def rechercher_client(code):
    for client in clients:
        if client.code_client == code:
            return client
    return None

def rechercher_produit(designation):
    for produit in produits:
        if produit.designation.lower() == designation.lower():
            return produit
    return None

def rechercher_commande(num):
    for cmd in commandes:
        if cmd.num_commande == num:
            return cmd
    return None

def menu():
    while True:
        print("\nMenu :")
        print("1- Ajouter client")
        print("2- Ajouter produit")
        print("3- Ajouter commande")
        print("4- Rechercher commande par numéro")
        print("5- Rechercher commandes par date")
        print("6- Quitter")
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            code = input("Code client : ")
            nom = input("Nom : ")
            adresse = input("Adresse : ")
            tel = input("Téléphone : ")
            email = input("Email : ")
            clients.append(Client(code, nom, adresse, tel, email))
            print("Client ajouté!")
        
        elif choix == "2":
            ref = input("Référence : ")
            des = input("Désignation : ")
            prix = float(input("Prix unitaire : "))
            stock = int(input("Quantité stock : "))
            produits.append(Produit(ref, des, prix, stock))
            print("Produit ajouté!")
        
        elif choix == "3":
            code = input("Code client : ")
            client = rechercher_client(code)
            if not client:
                print("Client introuvable!")
                continue
            
            commande = Commande(client)
            while True:
                des = input("Désignation produit : ")
                produit = rechercher_produit(des)
                if not produit:
                    print("Produit introuvable!")
                    continue
                
                quantite = int(input("Quantité : "))
                commande.ajouter_produit(produit, quantite)
                
                cont = input("Ajouter un autre produit ? (o/n) : ")
                if cont.lower() != "o":
                    break
            
            commandes.append(commande)
            print("Commande ajoutée!")
        
        elif choix == "4":
            num = int(input("Numéro de commande : "))
            commande = rechercher_commande(num)
            if commande:
                commande.afficher_commande()
            else:
                print("Commande introuvable!")
        
        elif choix == "5":
            date = input("Date (YYYY-MM-DD) : ")
            found = False
            for cmd in commandes:
                if cmd.date_commande == date:
                    print(cmd)
                    found = True
            if not found:
                print("Aucune commande trouvée pour cette date.")
        
        elif choix == "6":
            print("Au revoir!")
            break
        
        else:
            print("Option invalide!")

menu()
