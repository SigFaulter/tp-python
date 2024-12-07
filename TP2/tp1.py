class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
        
    def aboyer(self):
        print("Woof!")

chien = Chien("bob", "shepard", 4)
chien.aboyer()
