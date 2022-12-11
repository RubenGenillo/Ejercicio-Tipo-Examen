def movimiento(jugador, tabla):
    mover = True
    while mover:    
        c = inputint("¿En qué columna quieres mover la torre? (Introduce un número entero)\n", 0, len(tabla)-1)
        f = inputint("Que posición quieres que ocupe la torre? (Introduce un número entero negativo arriba y numero entero positivo hacia abajo)\n", -(len(tabla)), len(tabla))
        if f >=0:
            signo = 1
        else:
            signo = -1
        posiciono = tabla[c].index(jugador)
        posicion = tabla[c].index(jugador)
        for i in range(signo, f+signo, signo):
            if f < 0:
                posicion = posicion -1
                mover = False
            elif f > 0:
                posicion = posicion +1
                mover = False
            else:
                pass

            if (posiciono + f < 0 or posiciono + f > len(tabla)-1) or tabla[c][posicion] != 0:
                print("no puedes mover la torre a esa posicion")
                mover = True
                break
    
    tabla[c][posiciono] = 0
    tabla[c][posicion] = jugador
    return tabla

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def juego(tablero):
    jugador = True
    while True:
        mostrar_matriz(tablero)
        if not puede_moverse(jugador, tablero):
            return jugador
        tablero = movimiento(int(jugador) + 1, tablero)
        if jugador:
            jugador = False
        else:
            jugador = True

def puede_moverse(jugador, tabla):
    if jugador:
        posicion = tabla[0][1]
    else:
        posicion = tabla[0][len(tabla)-2]

    if posicion != (int(not jugador)+1):
        return True
    
    for c in range(len(tabla)-1):
        if jugador:
            posicion = tabla[c+1][len(tabla)-2]
        else:
            posicion = tabla[c+1][1]
        if posicion != (int(not jugador)+1):
            return True
    return False

def inputint(texto, min, max):
  while True:
    num = input(texto)
    try:
        num = int(num)
    except:
        pass 
    else:    
     if num <= max and num >= min:
         return num

def crea_tablero(n):
    tablero = []
    for i in range(n):
        tablero.append([])
        for j in range(n):
            tablero[i].append(0)
    return tablero

def poner_torres(tablero):
    for i in range(len(tablero)):
        tablero[i][0] = 1
        tablero[i][-1] = 2
    tablero[0].reverse()
    return tablero

def main():
    t = inputint("¿Cuántos partidas quieres jugar? (Introduce un número entero entre 1 y 10)\n", 1, 10)
    n = inputint("¿Cuántas casillas quieres que tenga el tablero? (Introduce un número entero entre 2 y 2000)\n", 2, 2000)
    for i in range(t):
        tablero = poner_torres(crea_tablero(n))
        ganador = juego(tablero)
        print(f"El ganador es el jugador {int(not ganador)+1}")

if __name__ == '__main__':
    main()
