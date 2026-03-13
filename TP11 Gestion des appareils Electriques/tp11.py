
class Appareil:
    def __init__(self, reference, puissance, poids, prix):
        self._reference = reference
        self._puissance = puissance
        self._poids = poids
        self._prix = prix

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value
    
    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, value):
        self._puissance = value
    
    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, value):
        self._poids = value
    
    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, value):
        self._prix = value
    
    def __str__(self):
        return (f"Référence: {self.reference}, Puissance: {self.puissance} W, "
                f"Poids: {self.poids} kg, Prix: {self.prix} €")

    def classe_energetique(self):
        if self.puissance < 300:
            return "Classe A"
        elif 300 <= self.puissance <= 1000:
            return "Classe B"
        else:
            return "Classe C"



class Television(Appareil):
    def __init__(self, reference, puissance, poids, prix, type_ecran, frequence):
        super().__init__(reference, puissance, poids, prix)
        self._type_ecran = type_ecran
        self._frequence = frequence

    @property
    def type_ecran(self):
        return self._type_ecran

    @type_ecran.setter
    def type_ecran(self, value):
        self._type_ecran = value
    
    @property
    def frequence(self):
        return self._frequence

    @frequence.setter
    def prix(self, value):
        self._frequence = value
    
    def __str__(self):
        return (super().__str__() + 
                f", Type d'écran: {self.type_ecran}, Fréquence: {self.frequence} Hz")


class VeloElec(Appareil):
    def __init__(self, reference, puissance, poids, prix, autonomie, kilometrage):
        super().__init__(reference, puissance, poids, prix)
        self._autonomie = autonomie
        self._kilometrage = kilometrage

    @property
    def autonomie(self):
        return self._autonomie

    @autonomie.setter
    def autonomie(self, value):
        self._autonomie = value
    
    @property
    def kilometrage(self):
        return self._kilometrage

    @kilometrage.setter
    def kilometrage(self, value):
        self._kilometrage = value
    
    
    def rouler(self, distance):
        if distance > self.autonomie:
            print("Impossible de parcourir la distance demandée : autonomie insuffisante.")
        else:
            self.autonomie -= distance
            self.kilometrage += distance
        return self.kilometrage

    def charger(self, nbr_minute):
        
        km_recharge = (nbr_minute / 60) * 10  
        self.autonomie += int(km_recharge)
        return self.autonomie

    def __str__(self):
       
        return (super().__str__() + 
                f", Autonomie: {self.autonomie} km, Kilométrage: {self.kilometrage} km")

if __name__ == "__main__":
    appareil = Appareil("APP123", 500, 10.5, 299.99)
    print(appareil)
    print(f"Classe énergétique : {appareil.classe_energetique()}")

    television = Television("TV456", 800, 15.2, 499.99, "LED", 120)
    print(television)
    print(f"Classe énergétique : {television.classe_energetique()}")

    velo = VeloElec("VELO789", 250, 20.0, 999.99, 50, 100)
    print(velo)

    print("\n--- Test Rouler ---")
    print(f"Kilométrage avant : {velo.kilometrage} km, Autonomie avant : {velo.autonomie} km")
    velo.rouler(30)
    print(f"Kilométrage après : {velo.kilometrage} km, Autonomie après : {velo.autonomie} km")

    print("\n--- Test Charger ---")
    print(f"Autonomie avant charge : {velo.autonomie} km")
    velo.charger(120) 
    print(f"Autonomie après charge : {velo.autonomie} km")