class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        
    def afficher_info(self):
        print(f"marque: {self.marque}, modele: {self.modele}, annee: {self.annee}")

voiture = Voiture("alfa romeo", "Stelvio", 2016)
voiture1 = Voiture("Volvo", "XC40", 2017)
voiture2 = Voiture("Ford", "427", 2003)
voiture.afficher_info()
voiture1.afficher_info()
voiture2.afficher_info()
