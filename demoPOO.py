
class Rectangle:
    def __init__(self, larg, long):
        # Constructeur de classe
        self.largeur = larg
        self.longueur = long
        self.epaisseur = 0.001 # Une valeur par défaut

    def __str__(self):
        return f"Rectangle {self.largeur} x {self.longueur} x {self.epaisseur}"

    def setEpaisseur(self, epaisseur):
        # Setter pour epaisseur
        self.epaisseur = epaisseur

    def surface(self):
        return self.largeur * self.longueur

    def volume(self):
        return self.epaisseur * self.surface()

r1 = Rectangle(1.1, 2.2)
print('mon rectangle:', r1)
print('Surface:', r1.surface())
print('Volume:', r1.volume())
r1.setEpaisseur(0.5)
print('Volume:', r1.volume())
print('mon rectangle:', r1)
