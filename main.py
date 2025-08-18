import random  
import os     


registro_partidas = []  


def limpiar_pantalla():
    # Limpia la consola dependiendo del sistema operativ0
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú principal
def mostrar_menu_inicial():
    limpiar_pantalla()  
    print("="*50)
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("="*50)
    print("1. Comenzar juego")  
    print("2. Ver instrucciones")  
    print("3. Salir")  
    print("="*50)

# Función para mostrar el menú de opciones del juego
def menu_opciones_juego():
    limpiar_pantalla()  
    print("===================================")
    print("Opciones de Juego")
    print("===================================")
    print("1. Jugar contra la computadora")  
    print("2. Jugar en pareja")  
    print("3. Ver estadísticas")  
    print("4. Regresar al menú principal")  
    print("===================================")

# Función para mostrar las reglas del juego
def mostrar_instrucciones():
    limpiar_pantalla()  
    print("\nReglas del juego:")
    print("1. Piedra vence a Tijeras.")  
    print("2. Tijeras vence a Papel.")  
    print("3. Papel vence a Piedra.")  
    print("4. El objetivo es ganar más rondas que tu oponente.\n")  
    input("Presiona Enter para volver al menú principal...")  

# Función para obtener la elección del jugador
def seleccionar_eleccion():
    while True:
        # Solicita al jugador que elija entre piedra, papel o tijeras
        eleccion = input("Elige entre piedra, papel o tijeras: ").lower()
        if eleccion in ["piedra", "papel", "tijeras"]:  # Verifica que la entrada sea válida
            return eleccion  # Retorna la elección si es válida
        else:
            print("Entrada inválida. Elige entre 'piedra', 'papel' o 'tijeras'.")  # Mensaje de error si la entrada no es válida

# Función para obtener la cantidad de rondas
def cantidad_de_rondas():
    rondas = input("¿Cuántas rondas deseas jugar? (Presiona Enter para continuar sin límite): ")
    if rondas.isdigit() and int(rondas) > 0:  # Verifica si la entrada es un número y es mayor que cero
        return int(rondas)  # Retorna el número de rondas
    else:
        return None  # Si no es válido, retorna None para continuar sin límite de rondas

# Función para validar si el jugador quiere seguir jugando
def seguir_jugando():
    while True:
        continuar = input("¿Quieres jugar otra ronda? (si/no): ").lower()  # Pregunta si el jugador quiere seguir jugando
        if continuar == "si":
            return True  # Si responde "si", permite continuar el juego
        elif continuar == "no":
            return False  # Si responde "no", termina el juego
        else:
            print("Entrada inválida. Por favor, elige 'si' o 'no'.")  # Si la respuesta no es válida, muestra un mensaje de error

# Función para jugar contra la computadora
def jugar_con_computadora():
    jugador_nombre = input("Ingresa tu nombre: ")  # Solicita el nombre del jugador
    puntos_jugador, puntos_computadora = 0, 0  # Inicializa los puntos del jugador y de la computadora
    rondas = cantidad_de_rondas()  # Obtiene la cantidad de rondas

    ronda_actual = 1  # Inicializa el contador de rondas
    while True:
        limpiar_pantalla()  # Limpia la pantalla en cada ronda
        print(f"\nRonda {ronda_actual}")  # Muestra el número de la ronda actual
        eleccion_jugador = seleccionar_eleccion()  # Obtiene la elección del jugador
        eleccion_computadora = random.choice(["piedra", "papel", "tijeras"])  # La computadora elige aleatoriamente
        print(f"La computadora eligió: {eleccion_computadora}")  # Muestra la elección de la computadora
        
        # Lógica para determinar el ganador de la ronda
        if eleccion_jugador == eleccion_computadora:
            print("¡Es un empate!")  # Si ambos eligen lo mismo, es un empate
        elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijeras") or \
             (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_jugador == "tijeras" and eleccion_computadora == "papel"):
            print(f"{jugador_nombre} gana esta ronda!")  # Si el jugador gana
            puntos_jugador += 1  # Aumenta los puntos del jugador
        else:
            print("La computadora gana esta ronda!")  # Si la computadora gana
            puntos_computadora += 1  # Aumenta los puntos de la computadora
        
        # Verifica si se alcanzó el número de rondas
        if rondas and ronda_actual >= rondas:
            break  # Si se alcanzó el límite de rondas, termina el juego
        if not rondas:
            if not seguir_jugando():  # Llama a la función para preguntar si desea seguir jugando
                break  # Si el jugador no quiere continuar, termina el juego
        else:
            input("Presiona Enter para continuar a la siguiente ronda...")  # Espera a que el jugador presione Enter
        ronda_actual += 1  #

    # Muestra el resultado final después de todas las rondas
    print(f"\nResultado final: {jugador_nombre}: {puntos_jugador} - Computadora: {puntos_computadora}")
    # Almacena las estadísticas de la partida en la lista global
    registro_partidas.append(f"Jugador: {jugador_nombre} | Rondas jugadas: {ronda_actual-1} | Ganó: {puntos_jugador} | Computadora: {puntos_computadora}")
    input("Presiona Enter para continuar...")


def jugar_en_pareja():
    jugador1_nombre = input("Ingresa el nombre del Jugador 1: ")  
    jugador2_nombre = input("Ingresa el nombre del Jugador 2: ")  
    puntos_jugador1, puntos_jugador2 = 0, 0  
    rondas = cantidad_de_rondas()  

    ronda_actual = 1  
    while True:
        limpiar_pantalla()  # Limpia la pantalla en cada ronda
        print(f"\nRonda {ronda_actual}")
        
        input(f"{jugador1_nombre}, presiona Enter para hacer tu elección...")  # Espera a que el jugador 1 presione Enter
        eleccion_jugador1 = seleccionar_eleccion()  # Obtiene la elección del jugador 1
        limpiar_pantalla()

        input(f"{jugador2_nombre}, presiona Enter para hacer tu elección...")
        eleccion_jugador2 = seleccionar_eleccion() 
        print(f"{jugador1_nombre} eligió: {eleccion_jugador1} | {jugador2_nombre} eligió: {eleccion_jugador2}")

        
        if eleccion_jugador1 == eleccion_jugador2:
            print("¡Es un empate!")
        elif (eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijeras") or \
             (eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra") or \
             (eleccion_jugador1 == "tijeras" and eleccion_jugador2 == "papel"):
            print(f"{jugador1_nombre} gana esta ronda!")  
            puntos_jugador1 += 1  
        else:
            print(f"{jugador2_nombre} gana esta ronda!")  
            puntos_jugador2 += 1  

       
        if rondas is not None and ronda_actual >= rondas:
            break  
        
        if rondas is None:
            if not seguir_jugando():  
                break  
        input("Presiona Enter para continuar...")  
        ronda_actual += 1  

    
    print(f"\nResultado final: {jugador1_nombre}: {puntos_jugador1} - {jugador2_nombre}: {puntos_jugador2}")
    
    registro_partidas.append(f"Jugador1: {jugador1_nombre} | Jugador2: {jugador2_nombre} | Rondas jugadas: {ronda_actual-1} | Ganó: {puntos_jugador1} | Ganó: {puntos_jugador2}")
    input("Presiona Enter para continuar...")

# Función para mostrar las estadísticas de las partidas jugadas
def ver_estadisticas():
    limpiar_pantalla()  
    if registro_partidas:  
        for partida in registro_partidas:  
            print(partida)
    else:
        print("No hay estadísticas disponibles.")  
    input("Presiona Enter para volver al menú principal...")


def ejecutar_juego():
    while True:
        mostrar_menu_inicial()  
        seleccion = input("Selecciona una opción: ")  

        if seleccion == "1":
            registro_partidas.clear()
            while True:
                menu_opciones_juego()  
                opcion_juego = input("Selecciona una opción del menú de juego: ")  

                if opcion_juego == "1":
                    jugar_con_computadora()  
                elif opcion_juego == "2":
                    jugar_en_pareja()  
                elif opcion_juego == "3":
                    ver_estadisticas()  
                elif opcion_juego == "4":
                    break  
                else:
                    print("Opción no válida.")  
        elif seleccion == "2":
            mostrar_instrucciones()  
        elif seleccion == "3":
            limpiar_pantalla()  
            print("¡Hasta la próxima!")
            break  
        else:
            print("Opción no válida.")  


ejecutar_juego()  

