#Proyecto final - Minijuego TATETI (Grupo: Juan Cruz - Mirko)
'''Reglamento:
1. Cantidad de jugadores: 2.
2. Objetivo: Formar TA-TE-TI en el tablero de juego.
3. El jugador que inicia el juego lo define el sistema en forma aleatoria.

Como jugar:
- Al inicio el sistema define en forma aleatoria cual de los 2 jugadores comienza la partida.
- Inicialmente, cada jugador podrá elegir 3 posiciones del tablero (que estén vacías), según se desarrolla
la partida.
- El jugador que comienza podrá elegir cualquier posición del tablero (incuida la del centro).
- Luego de la primer jugada, continua el otro jugador y así sucesivamente de forma alternada.
- Si no hay un ganador luego de elegidas las 3 posiciones del tablero por cada jugador,
el juego puede continuar dejando libre una posición del tablero y seleccionar otra distinta a esta, pero libre.
- La selección de nuevas posiciones por parte de ambos jugadores, será en función a como se
desarrolle la partida y finalizará cuando un de los jugadores logre formar TA-TE-TI.
'''
#Función de inicio - Define de forma aleatoria quien es "X" y "O" y quien comienza jugando en la partida.
import random

simbolos=["X","O"]

jug1=str(input('Ingresar nombre del jugador 1: '))
jug2=str(input('Ingresar nombre del jugador 2: '))

def ini_partida(x,y):
    jugadores=[jug1,jug2]
    asig1=(random.choice(simbolos))
    if asig1=='X':
        asig2='O'
    else:
        asig2='X'
    print('La asignación de letras para: ', jug1,' es ',asig1, ' y ', jug2, ' es ', asig2)
    print('Inicia la partida:',random.choice(jugadores))
    return ()

ini_partida(jug1,jug2)

def mostrar_tablero(tablero): # se crea función para crear el tablero e imprimirlo en pantalla
    for fila in tablero:
        for i in range (len (fila)): # recorre cada elemento de la fila
            if i==len(fila)-1: # representa el último elemento de cada lista,ya que el largo de cada sublista es de 3 elementos(len=2),ya que se cuenta desde subindice 0 a 2.
                print(fila[i],end='\n') # se muestra en pantalla sólo el último elemento de cada lista y con '\n' se baja al siguiente renglón, para armar el tablero
            else: # si no es el último elemento, se lo imprime en pantalla y no se baja a siguiente renglón
                print(fila[i], end=' ') 
tablero= [
    ['| 1','| 2 |','3 |'],
    ['-------------'],
    ['| 4','| 5 |','6 |'],
    ['-------------'],
    ['| 7','| 8 |','9 |'],
    
]
mostrar_tablero(tablero)

