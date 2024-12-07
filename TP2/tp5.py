class Animal:
    def faire_du_bruit(self):
        pass
    
class Chien(Animal):
    def faire_du_bruit(self):
        print("woof")
    
class Chat(Animal):
    def faire_du_bruit(self):
        print("meow")
        
Chat().faire_du_bruit()
Chien().faire_du_bruit()
