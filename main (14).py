import random  # Importa la librería 'random' para generar la jugada de la computadora de forma aleatoria 
import os     # Importa la librería 'os' para interactuar con el sistema operativo (en este caso, para limpiar la consola)

# Variables globales
registro_partidas = []  # Lista para almacenar las estadísticas de las partidas jugadas

# Función para limpiar la consola
def limpiar_pantalla():
    # Limpia la consola dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú principal
def mostrar_menu_inicial():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
    print("="*50)
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("="*50)
    print("1. Comenzar juego")  # Opción para comenzar a jugar
    print("2. Ver instrucciones")  # Opción para ver las reglas
    print("3. Salir")  # Opción para salir del juego
    print("="*50)

# Función para mostrar el menú de opciones del juego
def menu_opciones_juego():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú de juego
    print("===================================")
    print("Opciones de Juego")
    print("===================================")
    print("1. Jugar contra la computadora")  # Opción para jugar contra la computadora
    print("2. Jugar en pareja")  # Opción para jugar en pareja
    print("3. Ver estadísticas")  # Opción para ver las estadísticas
    print("4. Regresar al menú principal")  # Opción para volver al menú principal
    print("===================================")

# Función para mostrar las reglas del juego
def mostrar_instrucciones():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar las reglas
    print("\nReglas del juego:")
    print("1. Piedra vence a Tijeras.")  # Regla: Piedra vence a tijeras
    print("2. Tijeras vence a Papel.")  # Regla: Tijeras vence a papel
    print("3. Papel vence a Piedra.")  # Regla: Papel vence a piedra
    print("4. El objetivo es ganar más rondas que tu oponente.\n")  # Objetivo del juego
    input("Presiona Enter para volver al menú principal...")  # Espera que el jugador presione Enter para regresar al menú

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
        ronda_actual += 1  # Incrementa el contador de rondas

    # Muestra el resultado final después de todas las rondas
    print(f"\nResultado final: {jugador_nombre}: {puntos_jugador} - Computadora: {puntos_computadora}")
    # Almacena las estadísticas de la partida en la lista global
    registro_partidas.append(f"Jugador: {jugador_nombre} | Rondas jugadas: {ronda_actual-1} | Ganó: {puntos_jugador} | Computadora: {puntos_computadora}")
    input("Presiona Enter para continuar...")

# Función para jugar en pareja
def jugar_en_pareja():
    jugador1_nombre = input("Ingresa el nombre del Jugador 1: ")  # Solicita el nombre del jugador 1
    jugador2_nombre = input("Ingresa el nombre del Jugador 2: ")  # Solicita el nombre del jugador 2
    puntos_jugador1, puntos_jugador2 = 0, 0  # Inicializa los puntos de ambos jugadores
    rondas = cantidad_de_rondas()  # Obtiene la cantidad de rondas

    ronda_actual = 1  # Inicializa el contador de rondas
    while True:
        limpiar_pantalla()  # Limpia la pantalla en cada ronda
        print(f"\nRonda {ronda_actual}")
        
        input(f"{jugador1_nombre}, presiona Enter para hacer tu elección...")  # Espera a que el jugador 1 presione Enter
        eleccion_jugador1 = seleccionar_eleccion()  # Obtiene la elección del jugador 1
        limpiar_pantalla()

        input(f"{jugador2_nombre}, presiona Enter para hacer tu elección...")  # Espera a que el jugador 2 presione Enter
        eleccion_jugador2 = seleccionar_eleccion()  # Obtiene la elección del jugador 2

        print(f"{jugador1_nombre} eligió: {eleccion_jugador1} | {jugador2_nombre} eligió: {eleccion_jugador2}")

        # Lógica para determinar el ganador de la ronda
        if eleccion_jugador1 == eleccion_jugador2:
            print("¡Es un empate!")
        elif (eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijeras") or \
             (eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra") or \
             (eleccion_jugador1 == "tijeras" and eleccion_jugador2 == "papel"):
            print(f"{jugador1_nombre} gana esta ronda!")  # Si el jugador 1 gana
            puntos_jugador1 += 1  # Aumenta los puntos del jugador 1
        else:
            print(f"{jugador2_nombre} gana esta ronda!")  # Si el jugador 2 gana
            puntos_jugador2 += 1  # Aumenta los puntos del jugador 2

        # Verifica si se alcanzó el número de rondas
        if rondas is not None and ronda_actual >= rondas:
            break  # Si se alcanzó el límite de rondas, termina el juego
        
        if rondas is None:
            if not seguir_jugando():  # Llama a la función para preguntar si desea seguir jugando
                break  # Si el jugador no quiere continuar, termina el juego
        input("Presiona Enter para continuar...")  # Espera a que ambos jugadores presionen Enter para continuar
        ronda_actual += 1  # Incrementa el contador de rondas

    # Muestra el resultado final después de todas las rondas
    print(f"\nResultado final: {jugador1_nombre}: {puntos_jugador1} - {jugador2_nombre}: {puntos_jugador2}")
    # Almacena las estadísticas de la partida en la lista global
    registro_partidas.append(f"Jugador1: {jugador1_nombre} | Jugador2: {jugador2_nombre} | Rondas jugadas: {ronda_actual-1} | Ganó: {puntos_jugador1} | Ganó: {puntos_jugador2}")
    input("Presiona Enter para continuar...")

# Función para mostrar las estadísticas de las partidas jugadas
def ver_estadisticas():
    limpiar_pantalla()  # Limpia la pantalla antes de mostrar las estadísticas
    if registro_partidas:  # Verifica si hay estadísticas registradas
        for partida in registro_partidas:  # Muestra cada registro de partida
            print(partida)
    else:
        print("No hay estadísticas disponibles.")  # Muestra un mensaje si no hay estadísticas
    input("Presiona Enter para volver al menú principal...")

# Función principal que ejecuta el juego
def ejecutar_juego():
    while True:
        mostrar_menu_inicial()  # Muestra el menú inicial
        seleccion = input("Selecciona una opción: ")  # Solicita la opción elegida por el jugador

        if seleccion == "1":
            registro_partidas.clear()
            while True:
                menu_opciones_juego()  # Muestra las opciones de juego
                opcion_juego = input("Selecciona una opción del menú de juego: ")  # Solicita la opción del jugador

                if opcion_juego == "1":
                    jugar_con_computadora()  # Llama a la función para jugar contra la computadora
                elif opcion_juego == "2":
                    jugar_en_pareja()  # Llama a la función para jugar en pareja
                elif opcion_juego == "3":
                    ver_estadisticas()  # Muestra las estadísticas
                elif opcion_juego == "4":
                    break  # Regresa al menú principal
                else:
                    print("Opción no válida.")  # Mensaje si la opción no es válida
        elif seleccion == "2":
            mostrar_instrucciones()  # Muestra las instrucciones del juego
        elif seleccion == "3":
            limpiar_pantalla()  # Limpia la pantalla y termina el juego
            print("¡Hasta la próxima!")
            break  # Sale del juego
        else:
            print("Opción no válida.")  # Mensaje si la opción no es válida

# Ejecutar el juego
ejecutar_juego()  # Llama a la función principal para ejecutar el juego
