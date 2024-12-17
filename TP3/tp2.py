class Personne:
        def __init__(self, nom, prenom, age):
                self.__nom = nom
                self.__prenom = prenom
                self.__age = age

        def get_nom(self):
                return self.__nom

        def set_nom(self, nom):
            if nom.isalpha():
                self.__nom = nom
            else:
                print("Erreur: nom est pas une chaine de characteres")

        def get_prenom(self):
            return self.__prenom

        def set_prenom(self, prenom):
            if prenom.isalpha():
                self.__prenom = prenom
            else:
                print("Erreur: prenom est pas une chaine de characteres")

        def get_age(self):
            return self.__age

        def set_age(self, age):
            if isinstance(age, int): 
                self.__age = age
            else:
                print("Erreur: age est pas un nombre")

person = Personne("John", "idk", 22)
person.set_nom("test")
print(person.get_nom())
person.set_prenom("something")
print(person.get_prenom())
person.set_age(44)
print(person.get_age())


