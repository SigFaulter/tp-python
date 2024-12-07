class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication


class Bibliotheque:
    livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, annee de publication: {livre.annee_publication}")


livre1 = Livre("A. zavarelli", "Echo", 2015)
livre2 = Livre("Amy Silver", "The Reunion", 2013)

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)
biblio.afficher_livres()
