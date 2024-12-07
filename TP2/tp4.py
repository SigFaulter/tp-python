class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    def se_presenter(self):
        print(f"Nom: {self.nom}, Prenom: {self.prenom}, Age: {self.age}")
        
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        Personne.__init__(self, nom, prenom, age)
        self.matricule = matricule
        
    def etudier(self):
        pass
      
