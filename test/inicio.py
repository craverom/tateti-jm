#Función de inicio - Define de forma aleatoria quien es "X" e "O" y quien comienza jugando en la partida.
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
    print('La asignación de letras es: ', jug1,'=',asig1, '|', jug2, '=', asig2)
    print('Inicia la partida:',random.choice(jugadores))
    return ()

ini_partida(jug1,jug2)
debemos cambiar la matriz y agregarle los subindices

def mostrar_tablero(tablero): # se crea función para crear el tablero e imprimirlo en pantalla
    for fila in tablero:
        for i in range (len (fila)): # recorre cada elemento de la fila
            if i==len(fila)-1: # representa el último elemento de cada lista,ya que el largo de cada sublista es de 5 elementos(len=4),ya que se cuenta desde subindice 0 a 4.
                print(fila[i],end='\n') # se muestra en pantalla sólo el último elemento de cada lista y con '\n' se baja al siguiente renglón, para armar el tablero
            else: # si no es el último elemento, se lo imprime en pantalla y no se baja a siguiente renglón
                print(fila[i], end='  ') 
                tablero= [ 
    [ '|', ' ', '|', ' '], # posición 0,1,2,3,4 de la lista 0 [0:0,0:1,0:2,0:3,0:4]
    [ ' ', '-', ' ', '-'], # posición 0,1,2,3,4 de la lista 1 [1:0,1:1,1:2,1:3,1:4]
    [ '|', ' ', '|', ' '], # posición 0,1,2,3,4 de la lista 2 [2:0,2:1,2:2,2:3,2:4]
    ['-', ' ', '-', ' ', '-'], # posición 0,1,2,3,4 de la lista 3 [3:0,3:1,3:2,3:3,3:4]
    [ '|', ' ', '|', ' ']  # posición 0,1,2,3,4 de la lista 4 [4:0,4:1,4:2,4:3,4:4]
]

mostrar_tablero(tablero) # llama a la función para que se ejecute





