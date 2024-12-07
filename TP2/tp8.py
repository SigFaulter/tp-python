class Personne:
    amis = []
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def se_presenter(self):
        print(f"Nom: {self.nom}, Prenom: {self.prenom}, Age: {self.age}")

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        for ami in self.amis:
            print(f"Nom d'ami: {ami.nom}, Prenom d'ami: {ami.prenom}, Age d'ami: {ami.age}")

perso1 = Personne("Ahmed", "Charif", 23)
perso2 = Personne("John", "Doe", 24)
perso3 = Personne("Hamid", "Ali", 23)

perso1.ajouter_ami(perso2)
perso1.ajouter_ami(perso3)
perso1.afficher_amis()

