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
- 
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

def jugador_entrada():  #Con esta función, definimos los nombres de los jugadores, quien inicia (de forma aleatoria) y la jugada que realiza cada jugador.
    jug1=str(input('Ingresar nombre del jugador 1: ')) #Ejemplo: Mirko
    jug2=str(input('Ingresar nombre del jugador 2: ')) #Ejemplo: Juan
    
    jugadores=str([jug1,jug2]) #Definimos una lista con los nombre de los jugadores para usarla en la funcion random.choice. Ejemplo: Mirko, Juan
    
    #Definimos 3 variables auxiliares para elegir de forma aleatoria quien inicia y quien será el jugador1 y jugador2 (nombres), para luego sacarlos por pantalla.
    aux0=str(random.choice(jugadores)) #Pasamos la lista jugadores por la función choice para que defina en forma aleatoria que jugador comienza la partida.
    aux1=0 #Definimos una variable auxiliar1 y la iniciamos con cero.
    aux2=0 #Definimos una variable auxiliar2 y la iniciamos con cero.

<<<<<<< HEAD
    if aux0==jug1: #siguiendo con el ejemplo, compara que Mirko = Mirko, como se da esta situación el programa sigue en línea 55. Si se hubiese dado la situación inversa (Juan = Mirko) el programa pasa a la línea 57:
        aux1=str(jug1)  #confirma que aux1=Mirko
        aux2=str(jug2)  #confirma que aux2=Juan
    else:               
        aux1=str(jug2)  #confirma que aux1=Juan
        aux2=str(jug1)  #confirma que aux2=Mirko
    print('inicia la partida: '+aux1+' y luego sigue '+aux2+'\n'+ aux1+", elija un simbolo para jugar 'X' or 'O': ") #Saca por pantalla quien inicia y pide al jugador que inicia que elija que ficha va a utilizar 'X' o 'O'.

    #jugador1 = input("elija un simbolo para jugar 'X' or 'O': ")
    jugador1 = input()  #Soli
=======
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
>>>>>>> 20e85bb9ce54866be0ad18ae87af64410521b3a5
    
    while True:
        if jugador1.upper() == 'X':
            jugador2='O'
            print(aux1 + " usted elijio " + jugador1 + " entonces " + aux2 + " juega con " + jugador2)
            return jugador1.upper(),jugador2
        elif jugador1.upper() == 'O':
            jugador2='X'
            print(aux1 + "usted elijio " + jugador1 + " entonces " + aux2 + " juega con " + jugador2)
            return jugador1.upper(),jugador2
        else:
            jugador1 = input("Elija un simbolo para jugar 'X' or 'O' ")

def jugar(tablero, marcador_simbolo, posición):
    tablero[posición] = marcador_simbolo
    return tablero

def verificar_posicion(tablero, posición):
    return tablero[posición] == '_'

def verificar_tablero_vacio(tablero):
    #Section 21.2: Conditional List Comprehensions
    #[<expression> for <element> in <iterable> if <condition>]
    return len([x for x in tablero if x == '_']) == 1 

def verificar_3_en_linea(tablero, simbolo): #Con esta función, verificamos si hay 3 en línea (Ganador).
    if tablero[1] == tablero[2] == tablero[3] == simbolo: #condicionales para saber si hay 3 en línea (diagonales, verticales y horizontales)
        return True #Si hay 3 en línea, devuelve un True (verdadero), que sirve de entreda para el ciclo While del método principal.
    if tablero[4] == tablero[5] == tablero[6] == simbolo:
        return True
    if tablero[7] == tablero[8] == tablero[9] == simbolo:
        return True
    if tablero[1] == tablero[4] == tablero[7] == simbolo:
        return True
    if tablero[2] == tablero[5] == tablero[8] == simbolo:
        return True
    if tablero[3] == tablero[6] == tablero[9] == simbolo:
        return True
    if tablero[1] == tablero[5] == tablero[9] == simbolo:
        return True
    if tablero[3] == tablero[5] == tablero[7] == simbolo:
        return True
    return False    #si no hay 3 3n línea, devuelve un False (falso) que sirve de entrada para el ciclo while del método principal.

def eleccion_casilla(tablero):
    elegir = input("Seleccione una posicion vacia entre 1 y 9 : ")
    while not verificar_posicion(tablero, int(elegir)):
        elegir = input("Esta posicion ya esta ocupada. Seleccione una posicion vacia entre 1 y 9 : ")
    return elegir

def nueva_partida():
    nueva_jugada = input("Realizar una nueva partida (s/n)? ")
    if nueva_jugada.lower() == 'y':
        return True
    elif nueva_jugada.lower() == 'n':
        return False
    else:
        nueva_jugada = input("Realizar una nueva partida (s/n)? ")

if __name__ == "__main__": #Método principal para iniciar el programa.
    print('Mini juego TA-TE-TI | Grupo1: Juan Cruz - Mirko:')
    i = 1
    jugada=jugador_entrada() #asignamos la función "jugador_entrada" a la variable jugadores para llamarla cada vez que la necesitemos.
    tablero = ['_'] * 10 #definimos un tablero chato en forma de lista, creando un módulo '#' y replicandolo 10 veces.
    while True: # 
        inicio_partida=verificar_tablero_vacio(tablero) #llama a la función "verificar tablero lleno", para que arranque la partida siempre y cuando esté todo el tablero vacío |_|. Esto lo va hacer siempre!!
        while not inicio_partida: #Pide seleccionar la posición siempre y cuando este vacia.
            # El jugador elije donde colocar la ficha....
            posición = eleccion_casilla(tablero)
            # Quien esta jugando?
            if i % 2 == 0: #
                marcador_simbolo = jugada[1] #asigna 'X' si la partida es par.
            else:
                marcador_simbolo = jugada[0] #asigna 'O' si la partida es impar.
            # Jugar!
            jugar(tablero, marcador_simbolo, int(posición))
            # Verificar tablero
            mostrar_tablero(tablero)
            i += 1
            if verificar_3_en_linea(tablero, marcador_simbolo): #llama a la función "verificar_3_en_linea" para ver si hay ganador por medio de los codicionales.
                print("Usted ganó") # Agregar: que arroje el nombre del ganador!!
                break
            inicio_partida=verificar_tablero_vacio(tablero)
        if not nueva_partida(): #Función para preguntar si queremos realizar una nueva partida.
            break #Para finalizar el programa, eligiendo 'n'.
        else:
            i = 1
            jugada=jugador_entrada() #jugada toma el valor de la función.Elegir 'X' o 'O'.
            tablero = ['_'] * 10 # Inicio tablero vacio

