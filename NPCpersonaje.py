import random
import dado as d

class NPC:

    def __init__(self, nombre, vida, ataque, defensa):
        self.Nombre = nombre
        self.Vida = vida
        self.Ataque = ataque
        self.Defensa = defensa

    # Getters
    def obtener_Nombre(self):
        return self.Nombre

    def obtener_Vida(self):
        return self.Vida

    def obtener_Ataque(self):
        return self.Ataque

    def obtener_Defensa(self):
        return self.Defensa

    def to_dic(self):
        return vars(self)