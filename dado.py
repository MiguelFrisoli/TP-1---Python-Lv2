import random

class Dado:
    def __init__(self, numeroDeCaras):
        self.numeroDeCaras = numeroDeCaras

    def tirar_Dado (self):
        return random.randint(1, self.numeroDeCaras)


# d4 = Dado(4)
# d6 = Dado(6)
# d8 = Dado(8)
# d10= Dado(10)
# d12 = Dado(12)
# d20 = Dado(20)

# print(d4.tirar_Dado())
# print(d6.tirar_Dado())
# print(d8.tirar_Dado())
# print(d10.tirar_Dado())
# print(d12.tirar_Dado())
# print(d20.tirar_Dado())