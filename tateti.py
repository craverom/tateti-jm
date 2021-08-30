#Proyecto final - Minijuego TATETI (Grupo1: Juan Cruz - Mirko)
'''
Reglamento:
1. Cantidad de jugadores: 2.
2. Objetivo: Formar TA-TE-TI (3 fichas iguales en línea) en el tablero de juego.
3. El jugador que inicia el juego lo define el sistema en forma aleatoria.
4. Gana el primer jugador que logró colocar 3 fichas iguales en línea.
5. Si ningún jugador logró colocar 3 fichas iguales en línea y el tablero esta completo, la
partida se declara como empate.

Como jugar:
- Al inicio el sistema define en forma aleatoria cual de los 2 jugadores comienza la partida.
- El jugador que inicia elige si juega con 'X' o 'O'.
- Inicialmente, cada jugador podrá elegir 3 posiciones del tablero (que estén vacías), según
 se desarrolla la partida.
- El jugador que comienza podrá elegir cualquier posición del tablero (incuida la del centro).
- Luego de la primer jugada, continua el otro jugador y así sucesivamente de forma alternada
hasta ocupar todas las posiciones del tablero.
- El juego termina cuando uno de los jugadores haya logrado colocar 3 fichas iguales en línea o
se completó todas las posiciones del tablero sin ganador.
'''
import random #Importamos el módulo random para usar la función choice, para definir al azar quien inicia la partida.

def mostrar_tablero(tablero): #Con esta función definimos un tablero de referencia (cuales son las posiciones del 1 al 9) y le pasamos como parámetro el tablero de jugadas acumuladas. 
    tablero_vacio='''
-------------
| 1 | 2 | 3 |
|-----------|
| 4 | 5 | 6 |
|-----------|
| 7 | 8 | 9 |
-------------
'''
    for i in range(1,10):   #Mediante un ciclo for recorremos el tablero de jugadas acumuladas (tablero) y reseteamos el tablero de referencia colocando '_','X' o 'O' según corresponda.
        if (tablero[i] == 'O' or tablero[i] == 'X'):    #si en el tablero de jugadas acumuladas hay una 'X' o 'O', 
            tablero_vacio = tablero_vacio.replace(str(i), tablero[i])   #reseteamos el tablero_vacio, colocando una 'X' o 'O' en la posición que eligió el jugador.
        else:
            tablero_vacio = tablero_vacio.replace(str(i), ' ')  #si no hay coincidencia de 'X' o 'O', se resetea el tablero_vacio con '_' en la posición que eligió el jugador.
    print(tablero_vacio)    #sacamos por pantalla el tablero_vacio reseteado, mostrando las jugadas acumuladas.
    
def jugadores(jug1,jug2):
    
    jugadores=str([jug1,jug2]) #Definimos una lista con los nombre de los jugadores para usarla en la funcion random.choice. Ejemplo: Mirko, Juan
    
    #Definimos 3 variables auxiliares para elegir de forma aleatoria quien inicia y quien será el jugador1 y jugador2 (nombres), para luego sacarlos por pantalla.
    aux0=str(random.choice(jugadores)) #Pasamos la lista jugadores por la función choice para que defina en forma aleatoria que jugador comienza la partida.
    aux1=0 #Definimos una variable auxiliar1 y la iniciamos con cero.
    aux2=0 #Definimos una variable auxiliar2 y la iniciamos con cero.

    if aux0==jug1: #siguiendo con el ejemplo, compara que Mirko = Mirko, como se da esta situación el programa sigue en línea 55. Si se hubiese dado la situación inversa (Juan = Mirko) el programa pasa a la línea 57:
        aux1=str(jug1)  #confirma que aux1 toma el valor de jug1. Ejemplo: Mirko
        aux2=str(jug2)  #confirma que aux2 toma el valor de jug2. Ejemplo: Juan
    else:               
        aux1=str(jug2)  #confirma que aux1 toma el valor de jug2. Ejemplo: Juan
        aux2=str(jug1)  #confirma que aux2 toma el valor de jug1. Ejemplo: Mirko
    return aux1,aux2

def jugador_entrada(aux1,aux2):  #Con esta función, definimos los nombres de los jugadores, quien inicia (de forma aleatoria) y la jugada que realiza cada jugador.
    print('inicia la partida: ',aux1,' y luego sigue ',aux2,'\n',aux1,", elija un simbolo para jugar 'X' or 'O': ") #Saca por pantalla quien inicia y pide al jugador que inicia que elija que ficha va a utilizar 'X' o 'O'.
       
    jugador1 = input()  #Solicita al jugar que inicia la partida, que elija una posición "X" o "O".
    
    while True:
        if jugador1.upper() == 'X':
            jugador2='O'
            print(aux1, " usted elijio " , jugador1 , " entonces " , aux2 , " juega con " , jugador2)
            return jugador1.upper(),jugador2,aux1,aux2
        elif jugador1.upper() == 'O':
            jugador2='X'
            print(aux1 , " usted elijio " , jugador1 , " entonces " , aux2 , " juega con " , jugador2)
            return jugador1.upper(),jugador2,aux1,aux2
        else:
            jugador1 = input("Elija un simbolo para jugar 'X' or 'O' ")

def jugar(tablero, marcador_simbolo, posición): #función para asignar las X y las O, en cada posición del tablero lineal. 
    tablero[posición] = marcador_simbolo #el valor de la posición elegida por el jugador, tomar el valor de X para el jugador1 y O para el jugador2.
    return tablero #la función retorna un tablero juagdas acumuladas en forma de lista ['_', 'O', '_', '_', '_', 'X', '_', '_', '_', '_'], con las posiciones elegidas por caga jugador.

def verificar_posicion(tablero, posición): #función para verificar si la posición elegida está vacía.
    return tablero[posición] == '_' #nos retorna un tablero en forma de lista si la posición elegida está libre.

def verificar_tablero_vacio(tablero):
    #Section 21.2: Conditional List Comprehensions
    #[<expression> for <element> in <iterable> if <condition>]
    return len([x for x in tablero if x == '_']) == 1 

def verificar_3_en_linea(tablero,simbolo): #Con esta función, verificamos si hay 3 en línea (Ganador).
    if tablero[1] == tablero[2] == tablero[3] == simbolo: #condicionales para saber si hay 3 en línea (diagonales, verticales y horizontales). verifica si hay 3 en línea horizontal posiciones 1-2-3
        return True #Si hay 3 en línea, devuelve un True (verdadero), que sirve de entreda para el ciclo While del método principal.
    if tablero[4] == tablero[5] == tablero[6] == simbolo: #verifica si hay 3 en línea horizontal posiciones 3-4-5.
        return True
    if tablero[7] == tablero[8] == tablero[9] == simbolo: #verifica si hay 3 en línea horizontal posiciones 7-8-9.
        return True
    if tablero[1] == tablero[4] == tablero[7] == simbolo: #verifica si hay 3 en línea vertical posiciones 1-4-7.
        return True
    if tablero[2] == tablero[5] == tablero[8] == simbolo: #verifica si hay 3 en línea vertical posiciones 2-5-8.
        return True
    if tablero[3] == tablero[6] == tablero[9] == simbolo: ##verifica si hay 3 en línea vertical posiciones 3-6-9.
        return True
    if tablero[1] == tablero[5] == tablero[9] == simbolo: #verifica si hay 3 en línea oblicuo-izquierda posiciones 1-5-9.
        return True
    if tablero[3] == tablero[5] == tablero[7] == simbolo: ##verifica si hay 3 en línea oblicuo-derecha posiciones 3-5-7.
        return True
    return False    #si no hay 3 en línea, devuelve un False (falso) que sirve de entrada para el ciclo while del método principal.

def eleccion_casilla(tablero):
    elegir = input("Seleccione una posicion vacia entre 1 y 9 : ")
    while not verificar_posicion(tablero, int(elegir)):
        elegir = input("Esta posicion ya esta ocupada. Seleccione una posicion vacia entre 1 y 9 : ")
    return elegir

def nueva_partida(): #Función para determinar y queremos realizar una nueva patida o no, independientemente del resultado (empate o ganador).
    nueva_jugada = input("Realizar una nueva partida (s/n)? ") #solicitamos ingresar por teclado un s=si o n=no. 
    if nueva_jugada.lower() == 's': #si ingresamos "s", el condicional retorna un "verdadero" que sirve como entrada para el método principal y se vuelve a ejecutar todo el proceso nuevamente.
        return True
    elif nueva_jugada.lower() == 'n': #si ingresamos "n", el condicional devuelve un Falso.
        return False
    else:
        nueva_jugada = input("Realizar una nueva partida (s/n)? ") #para cualquier otra letra elegida que no sea s/n, volvemos a preguntar.

if __name__ == "__main__": #Método principal para iniciar el programa.
    print('Mini juego TA-TE-TI | Grupo1: Juan Cruz - Mirko:') #Sacamos por pantalla el título del mini juego.
    jug1=str(input('Ingresar nombre del jugador 1: ')) #Ejemplo: Mirko
    jug2=str(input('Ingresar nombre del jugador 2: ')) #Ejemplo: Juan
    
    i = 1 #iniciamos el contador de jugadas en 1.    
    jugadores(jug1,jug2)
    aux1,aux2=jugadores(jug1,jug2)
    jugada=jugador_entrada(aux1,aux2) #asignamos la función "jugador_entrada" a la variable jugadores para llamarla cada vez que la necesitemos.   
    tablero = ['_'] * 10 #definimos un tablero chato en forma de lista, creando un módulo '#' y replicandolo 10 veces.
    
    while True: #Ciclo while anidado para repetir las fuciones las n veces correspondientes a las jugadas.
        inicio_partida=verificar_tablero_vacio(tablero) #llama a la función "verificar tablero lleno", para que arranque la partida siempre y cuando esté todo el tablero vacío |_|. Esto lo va hacer siempre!!
        while not inicio_partida: #Pide seleccionar la posición siempre y cuando este vacia.  
            posición = eleccion_casilla(tablero) # llamos a la finción "eleccion_casilla", para que el jugador elija donde colocar la ficha....
            if i % 2 == 0: #con esta operación (división por % --> resto), asignamos 1 a las jugadas impares (juagador1) y 0 a las pares (jugador2) 
                marcador_simbolo = jugada[1] #las jugadas impares toman el valor 1.
            else:
                marcador_simbolo = jugada[0] #las jugadas pares toman el valor 0.
            # Jugar!!!
            jugar(tablero, marcador_simbolo, int(posición)) #llamamos a la función jugar y le pasamos los parámetros de referencia.
            mostrar_tablero(tablero) #llamamos a la función mostrar_tablero y pasamos el parámetro tablero.
            i += 1 #sumamos 1 al contador cada vez que se realiza una jugada.
            if verificar_3_en_linea(tablero,marcador_simbolo): #llama a la función "verificar_3_en_linea" para ver si hay ganador por medio de los codicionales.
                print("Usted ganó")
                break
            inicio_partida=verificar_tablero_vacio(tablero)
        if not nueva_partida(): #llamamos a la función "nueva_partida", para preguntar si queremos realizar una nueva partida.
            print("Fin del programa") #si en la función retorna un Falso, imprimimos por pantalla "Fin del programa"
            break #y con este break, interrumpimos el programa evitando que se ejecute nuevamente el ciclo while del método principal.
        else: #si la función "nueva_partida", nos retorna un "verdadero" continua ejecutandose el programa.
            i = 1 #reseteamos el contador i a 1 y continuamos con el ciclo while....
            jugada=jugador_entrada(aux1,aux2) #jugada toma el valor de la función. Elegir 'X' o 'O'.
            tablero = ['_'] * 10 # Inicio tablero vacio.

