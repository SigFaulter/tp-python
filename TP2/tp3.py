class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
        
    def deposer(self, montant):
        self.solde += montant
    
    def retirer(self, montant):
        self.solde -= montant
        
    def afficher_solde(self):
        print(f"Solde: {self.solde}")
        
compte = CompteBancaire("Ahmed", 99999)
compte.afficher_solde()
compte.deposer(1)
compte.afficher_solde()
compte.retirer(1)
compte.afficher_solde()
