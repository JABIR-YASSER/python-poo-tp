import re
class Personne:
    def __init__(self, mail):
        self.__mail = "Mail non valide" 
        if self.valider_mail(mail):
            self.__mail = mail       
        
    @property
    def mail(self):
        return self.__mail
    
    @mail.setter
    def mail(self,mail):        
        if self.valider_mail(mail):
            self.__mail = mail
        else:
            print("Mail non valide")
        
    def valider_mail(self, mail):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(regex, mail))
        
    def __str__(self):
        return f"Mail:{self.mail}"

mail = input("Mail ?: ")
p=Personne(mail)
print(p)
"""

Pour valider une adresse e-mail à l'aide d'une expression régulière (regex), une expression couramment utilisée est la suivante :

less
Copy code
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
Explication de cette expression regex :

^ : Début de la chaîne.
[a-zA-Z0-9._%+-]+ : Un ou plusieurs caractères parmi des lettres (majuscules ou minuscules), des chiffres, des points, des underscores, des pourcentages, des signes plus, et des tirets.
@ : Le symbole arobase, caractéristique des adresses e-mail.
[a-zA-Z0-9.-]+ : Un ou plusieurs caractères parmi des lettres, des chiffres, des points et des tirets pour le nom de domaine.
\. : Un point littéral.
[a-zA-Z]{2,} : Deux caractères ou plus parmi des lettres pour le suffixe de domaine (comme .com, .org, etc.).
$ : Fin de la chaîne.
"""
        
