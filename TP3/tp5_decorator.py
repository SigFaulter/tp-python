class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire


class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self._employe_supervises = [] # to fix recursion error calling the setter which calls the getter which loops there indefintely

    @property
    def employe_supervises(self):
        return self._employe_supervises 

    @employe_supervises.setter
    def employe_supervises(self, employe):
        self.employe_supervises.append(employe)

manager = Manager("Le", "manager", 999999)
employe = Employe("Employe", "1", 10000)
employe2 = Employe("Employe", "2", 10000)

manager.employe_supervises = employe
manager.employe_supervises = employe2

print("les employes supervise sont: ")
for emp in manager.employe_supervises:
    print(f"Nom: {emp.nom}, Prenom: {emp.prenom}, Salaire: {emp.salaire}")
