from PCpersonaje import Personaje
from NPCpersonaje import NPC
import random
import dado as d

print ("Bienvenido al juego, estás por enfrentarte a una serie de retos que te pueden costar la vida, espero que estés listo y por listo quiero decir, armas afiladas y armadura aceitada, pues los combates que trendrás no seran fáciles... aunque ahora que lo pienso seguramente terminarás decorando el piso con con tus huesos.... Jajajajaja")
nombre_jugador = input ("Como te llamas?... no es que me importe, tampoco creo que lo recuerde mucho tiempo... jejejeje"+"\n")    

#Llamo al metodo dado que me va a servir poara crear el PJ
d100 = d.Dado (100)
d20 = d.Dado (20)
d12 = d.Dado (12)
d10 = d.Dado (10)
d8 = d.Dado (8)
d6 = d.Dado (6)
d4 = d.Dado (4)
    
#Creo la variable jugador que nace de la clase personaje
jugador = Personaje(nombre_jugador, d12.tirar_Dado()*10+25, d20.tirar_Dado()+10, d8.tirar_Dado()*3+10)

#Crear el repertorio de mounstros y una variable para elegirlos al azar
goblin = NPC("Goblin",d4.tirar_Dado()*10,10,10)
esqueleto = NPC("Esqueleto",d6.tirar_Dado()*10,12,12)
zombie = NPC("Zombie",d8.tirar_Dado()*10,14,14)
orco = NPC("Orco",d10.tirar_Dado()*10,16,16)
troll = NPC("Troll",d20.tirar_Dado()*10,18,18)
bandido = NPC("Bandido",d20.tirar_Dado()*5,12,12)
asesino = NPC("Asesino",d20.tirar_Dado()*10,16,16)
guerrero = NPC("Guerrero",d20.tirar_Dado()*10,18,18)
minotauro = NPC("Minotauro",d20.tirar_Dado()*15,20,20)
dragon = NPC ("Dargon",d100.tirar_Dado()+d20.tirar_Dado()*20+d10.tirar_Dado()*5,25,25)

lista_Enemigos = [goblin,esqueleto,zombie,orco,troll,bandido,asesino,guerrero,minotauro,dragon]

enemigo = lista_Enemigos.pop(lista_Enemigos.index(random.choice(lista_Enemigos)))

print ("Muy bien", nombre_jugador," solo para que lo sepas... asi de débil eres:"+"\n")
print(f"(Vida: {jugador.obtener_Vida()}, Ataque: {jugador.obtener_Ataque()}, Defensa: {jugador.obtener_Defensa()})")
print("Tu primer desafío será:")
print(f"{enemigo.obtener_Nombre()} (Vida: {enemigo.obtener_Vida()}, Ataque: {enemigo.obtener_Ataque()}, Defensa: {enemigo.obtener_Defensa()})")
# print(jugador)
# print (enemigo)
# print(f"{jugador.obtener_Nombre()} (Vida: {jugador.obtener_Vida()}, Ataque: {jugador.obtener_Ataque()}, Defensa: {jugador.obtener_Defensa()})")
# print(f"{enemigo.obtener_Nombre()} (Vida: {enemigo.obtener_Vida()}, Ataque: {enemigo.obtener_Ataque()}, Defensa: {enemigo.obtener_Defensa()})")

#Crear el Metodo combate

def combate():
    global jugador
    global enemigo
    
    enemigo = enemigo.to_dic()
    d20 = d.Dado(20)
    vida_inicial_Jugador = jugador["Vida"]

    while True:
        accion_jugador = input("¿Quieres atacar o defender? ")
        if accion_jugador.lower() == "atacar":
            # El jugador ataca al enemigo
            defensa_enemigo = enemigo["Defensa"]
            defensa_jugador = jugador ["Defensa"]
            danio_jugador = jugador["Ataque"]+d20.tirar_Dado() - defensa_enemigo
            if danio_jugador > 0:
                enemigo["Vida"] -= danio_jugador
                print("¡Le has hecho", danio_jugador, "de daño al enemigo!")
            else:
                print("El enemigo ha bloqueado tu ataque.")
        elif accion_jugador.lower() == "defender":
            # El jugador se defiende
            defensa_jugador = jugador ["Defensa"]
            defensa_jugador *= 2
            print("Te has preparado para la defensa.")
        else:
            print("No entiendo esa acción.")
            continue
        
        # El enemigo ataca o se defiende al azar
        accion_enemigo = random.choice(["atacar", "defender"])
        if accion_enemigo == "atacar":
            defensa_jugador = jugador["Defensa"]
            defensa_enemigo = enemigo["Defensa"]
            danio_enemigo = enemigo["Ataque"]+d20.tirar_Dado() - defensa_jugador
            if danio_enemigo > 0:
                jugador["Vida"] -= danio_enemigo
                print("¡El enemigo te ha hecho", danio_enemigo, "de daño!")
            else:
                print("Has bloqueado el ataque del enemigo.")
        else:
            defensa_enemigo = enemigo["Defensa"]
            defensa_enemigo *= 2

            print("El enemigo se ha preparado para la defensa.")
        
        # Se comprueba si alguien ha perdido
        if jugador["Vida"] <= 0:
            print("¡Has perdido!")
            break
        elif enemigo["Vida"] <= 0:
            jugador["Vida"]= vida_inicial_Jugador+10 #subir vida
            jugador["Ataque"]+=2 #subir ataque
            jugador["Defensa"]+=2 #subir defensa
            print("¡Has ganado!")
            print("Has mejorado tu vida a:", jugador["Vida"])
            print("Has mejorado tu ataque a:", jugador["Ataque"])
            print("Has mejorado tu defensa a:", jugador["Defensa"])
            break
        else:
            print("Tu vida:", jugador["Vida"], "Vida del enemigo:", enemigo["Vida"])
#PRUEBA DE COMBATE
jugador = jugador.to_dic()

while lista_Enemigos != []:
    combate()
    print("Muy bien, has sobrevivido. Ahora toca el siguiente enemigo:")
    enemigo = lista_Enemigos.pop(lista_Enemigos.index(random.choice(lista_Enemigos)))
    print(f"{enemigo.obtener_Nombre()} (Vida: {enemigo.obtener_Vida()}, Ataque: {enemigo.obtener_Ataque()}, Defensa: {enemigo.obtener_Defensa()})")
    if lista_Enemigos == []:
        print("Maldito seas", nombre_jugador, "has ganado el dungeon, no quedan enemigos por vencer"+"\n"+"\n"+"VICTORIA"+"\n"+"\n"+"HAS GANADO")