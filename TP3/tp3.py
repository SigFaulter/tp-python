from tp1 import Cercle, Rectangle


def afficher_surface(formes):
    for form in formes:
        print(form.calculer_surface())

formes = []

rectangle = Rectangle(2, 3)
rectangle2 = Rectangle(4, 7)
cercle = Cercle(3)
cercle2 = Cercle(5)
formes.append(rectangle)
formes.append(rectangle2)
formes.append(cercle)
formes.append(cercle2)

afficher_surface(formes)
