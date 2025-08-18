# Piedra, Papel o Tijera

Este proyecto en Python es una implementación interactiva del clásico juego de **Piedra, Papel o Tijera**, donde puedes desafiar a la computadora o jugar en pareja. El juego es ideal para practicar lógica condicional, interacción con el usuario y cómo manejar ciclos y funciones en consola.

## Autora

Arianna Lara

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Instala las dependencias requeridas mediante el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
````

## Cómo jugar

### Iniciar el juego

1. **Ejecuta el archivo principal** desde la terminal:

```bash
python main.py
```

2. Aparecerá el **menú principal** con las siguientes opciones:

   * **Comenzar juego**: Inicia una nueva partida.
   * **Ver instrucciones**: Muestra las reglas del juego.
   * **Salir**: Finaliza el programa.

### Modos de juego

* **Jugar contra la computadora**:

  * En este modo, el jugador elige entre **Piedra**, **Papel** o **Tijeras** y se enfrenta a la computadora.
  * La computadora también elige una opción aleatoria y el ganador de la ronda se determina según las reglas tradicionales.
  * El juego sigue por varias rondas hasta que el jugador decida terminar o alcance el número de rondas deseadas.

* **Jugar en pareja**:

  * En este modo, dos jugadores se turnan para elegir entre **Piedra**, **Papel** o **Tijeras**.
  * Cada ronda se evalúa y se otorgan puntos al ganador. El juego continúa hasta el número de rondas especificado o hasta que un jugador decida salir.

### Reglas del juego

1. **Piedra** vence a **Tijeras**.
2. **Tijeras** vence a **Papel**.
3. **Papel** vence a **Piedra**.
4. El objetivo es ganar más rondas que tu oponente.

### Estadísticas

* Después de cada partida, se almacenan las estadísticas de las rondas jugadas, los puntos obtenidos por el jugador y la computadora (en el caso de jugar contra la computadora), o los puntos obtenidos por cada jugador (si es en pareja).
* Puedes consultar estas estadísticas desde el menú del juego.

## Estructura del código

* **Funciones principales**:

  * `mostrar_menu_inicial`: Muestra el menú de inicio del juego.
  * `menu_opciones_juego`: Muestra las opciones de juego (jugador contra computadora, multijugador, estadísticas).
  * `mostrar_instrucciones`: Muestra las reglas del juego.
  * `seleccionar_eleccion`: Permite al jugador elegir entre **Piedra**, **Papel** o **Tijeras**.
  * `cantidad_de_rondas`: Solicita y valida la cantidad de rondas a jugar.
  * `jugar_con_computadora`: Lógica para jugar contra la computadora.
  * `jugar_en_pareja`: Lógica para jugar en pareja.
  * `ver_estadisticas`: Muestra las estadísticas de las partidas jugadas.

## ¡Diviértete y desafía a tus amigos o a la computadora!
