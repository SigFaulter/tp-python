class Personne:
        def __init__(self, nom, prenom, age):
                self.__nom = nom
                self.__prenom = prenom
                self.__age = age

        @property
        def nom(self):
                return self.__nom

        @nom.setter
        def nom(self, nom):
            if nom.isalpha():
                self.__nom = nom
            else:
                print("Erreur: nom est pas une chaine de characteres")

        @property
        def prenom(self):
            return self.__prenom
        
        @prenom.setter
        def prenom(self, prenom):
            if prenom.isalpha():
                self.__prenom = prenom
            else:
                print("Erreur: prenom est pas une chaine de characteres")

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            if isinstance(age, int):
                self.__age = age
            else:
                print("Erreur: age est pas un nombre")

person = Personne("John", "idk", 22)
person.nom = "test"
print(person.nom)
person.prenom = "something"
print(person.prenom)
person.age = 44
print(person.age)

