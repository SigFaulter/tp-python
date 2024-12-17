from abc import ABC, abstractmethod

class Forme(ABC):
	@abstractmethod
	def calculer_surface(self):
		pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return (self.rayon ** 2) * 3.14

class Rectangle(Forme):
    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur

    def calculer_surface(self):
        return self.longeur * self.largeur 

if __name__ == '__main__':
    cercle = Cercle(3).calculer_surface()
    rectangle = Rectangle(2, 3).calculer_surface()

    print(f"surface de cercle est: {cercle}")
    print(f"surface de rectangle est: {rectangle}")
