class Produit:
    MONTANT_REMISE = 1000

    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix
    
    @property
    def nom(self):
        return self.__nom

    @property
    def prix(self):
        return self.__prix
    
    def remise(self, remise):
        if self.__prix > self.MONTANT_REMISE:
            self.__prix -= remise
        else:
            print(f"remise pas valabe pour les produit ayant un prix inferieur a {MONTANT_REMISE}")

if __name__ == '__main__':
    prod = Produit("Something", 1001)
    prod.remise(500)
    print(f"prix de produit apres remise: {prod.prix}")
