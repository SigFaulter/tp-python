class Vehicule:
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture se deplace")

class Bicyclette(Vehicule):
    def deplacer(self):
        print("La bicyclette se deplace")

voiture = Voiture()
voiture.deplacer()
bicyclette = Bicyclette()
bicyclette.deplacer()

