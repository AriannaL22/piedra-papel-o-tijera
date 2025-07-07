print ("Piedra, papel o tijeras esta por empezar")
import random
tus_puntos=0
puntospsp=0
ini=["Iniciar","Terminar"]
while True:
    print('Escriba "Iniciar" para iniciar el juego''\no "Terminar" para terminar el juego')
    elec=["piedra","papel","piedra"]
    inielec=input("[Iniciar|Terminar]:\n")
    if inielec == "Terminar":
        print("El juego termino")
        break
    elif inielec == "Iniciar":
        print("Iniciando juego")
        elejuego = input("Elige piedra, papel o tijeras:\n").lower()
        element = random.choice(elec)
        print("La máquina eligió:",element)
        
        if elejuego == element:
            print("¡Empate!\n")
        elif ((elejuego == "piedra" and element == "tijeras") or (elejuego == "papel" and element == "piedra") or (elejuego == "tijeras" and element == "papel")):
            print("Ganaste.")
            tus_puntos += 1
            print("Tú:",tus_puntos)
            print("Maquina:",puntospsp)
        else:
            print("Perdiste...\n")
            puntospsp += 1
            print("Tú:",tus_puntos)
            print("Maquina:",puntospsp)
        continue
    else:
        print("No existe esta opcion.")
        continue
    
print("Resultado:")
if tus_puntos > puntospsp:
    print("¡Ganaste el juego!")
    print("Tu puntaje:",tus_puntos)
    print("Estos los los puntos del bot:", puntospsp)

elif tus_puntos < puntospsp:
    print("El bot ganó.")
    print("Tu puntaje:", tus_puntos)
    print("Estos los los puntos del bot:", puntospsp)
else:
    print("Es un empate")
    print("Tu puntaje:",tus_puntos)
    print("Estos los los puntos del bot:", puntospsp)