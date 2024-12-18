class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"marque: {self.marque}, modele: {self.modele}, annee: {self.annee}")


class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_info(self):
        print(f"puissance: {self.puissance}, type moteur: {self.type_moteur}")


class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        self.vehicule = Vehicule(marque, modele, annee)
        self.moteur = Moteur(puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        print(f"nombre de places: {self.nombre_de_places}")


class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        self.vehicule = Vehicule(marque, modele, annee)
        self.moteur = Moteur(puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        print(f"type moto: {self.type_moto}")

voiture = Voiture("Hyundai", "iX20", 2015, 89, "1.6 CRDi", 4)
voiture.afficher_info()
voiture.vehicule.afficher_info()
voiture.moteur.afficher_info()

moto = Moto("BMW", "M 1000 RR", 2021, 205, "ShiftCam", "Sport")
moto.afficher_info()
moto.vehicule.afficher_info()
moto.moteur.afficher_info()
