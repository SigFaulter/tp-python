class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    def calculer_surface(self):
        print(f"{self.hauteur * self.largeur}")
        
    def calculer_perimetre(self):
        print(f"{(self.hauteur + self.largeur) * 2}")
        
rectangle = Rectangle(3, 4)
rectangle.calculer_perimetre()
rectangle.calculer_surface()
