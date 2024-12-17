from tp4 import Produit

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite


class Panier:
    def __init__(self):
        self.commandes = []

    def add_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        total = 0
        for command in self.commandes:
            total += command.produit.get_prix() * command.quantite

        return total

prod1 = Produit("Chaise", 60)
prod2 = Produit("Souris", 30)
prod3 = Produit("Tapis", 15)

panier = Panier()

command1 = Commande(prod1, 2)
command2 = Commande(prod2, 3)
command3 = Commande(prod3, 4)

panier.add_commande(command1)
panier.add_commande(command2)
panier.add_commande(command3)

print(f"total des prix des commandes est: {panier.calculer_total()}")
