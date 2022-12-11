def input_lleno(texto):
  while True:
    pal = input(texto)
    try:
        num = pal[0]
    except:
        pass
    else:    
     return pal

def ganador(puntos1, puntos2, jugador1, jugador2):
    if puntos1 > puntos2:
        return f"{jugador1} gana con {puntos1} puntos"
    elif puntos1 < puntos2:
        return f"{jugador2} gana con {puntos2} puntos"
    else:
        return "Draw"

def pedir_subcadenas(jugador, string, empezar_con):
    lista_subcadenas = []
    while True:
        palabra = input_lleno(f"{jugador} dame una subcadena nueva:\n").lower()
        if empezar_con == "consonante" and palabra[0] not in "aeiou" or empezar_con == "vocal" and palabra[0] in "aeiou":
            if palabra in string and palabra not in lista_subcadenas:
                    lista_subcadenas.append(palabra)
            else:
                print("escribe una palabra que este en la cadena y que no hayas escrito antes")
        else:
            print(f"escribe una palabra que empiece por {empezar_con}")
        continuar = input("Quieres se te ocurren más palabras? (s/n)\n")
        if continuar.lower() == "n":
            return lista_subcadenas
        elif continuar.lower() != "s":
            print("escribe s o n")

def cuenta_substring(subcadena, string):
    suma = 0
    for i in subcadena: 
        suma = suma + string.count(i)
    return suma

def minion_game(string):
    jugador1 = input("dame el nombre del jugador 1:\n")
    jugador2 = input("dame el nombre del jugador 2:\n")
    print(f"La palabra es {string}")
    subcadenajugador1 = pedir_subcadenas(jugador1, string, "consonante")
    subcadenajugador2 = pedir_subcadenas(jugador2, string, "vocal")   
    puntos_j_1 =cuenta_substring(subcadenajugador1, string)
    puntos_j_2 =cuenta_substring(subcadenajugador2, string)
    return ganador(puntos_j_1, puntos_j_2, jugador1, jugador2)

if __name__ == '__main__':
    print(minion_game("banana"))