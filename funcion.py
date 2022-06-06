import random,os
graficos = ['''
      _____
      |   |
          |
          |
          |
          |
    =========''', '''
      _____
      |   |
      O   |
          |
          |
          |
    =========''', '''
      _____
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      _____
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      _____
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      _____
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      _____
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

def bienvenida(pistas):
    os.system('clear')
    print("\033[;32m"+ f"A    H   O   R   C   A   D   O       {pistas} pistas")
    print("\033[;31m")
    print(graficos[6])
    print("\033[;37m")
    print("Escoja su nivel de dificultad:   ")
    print("\033[;32m"+"1. Facil")
    print("\033[;33m" + "2. Medio")
    print("\033[;31m" + "3. Dificil")
    print("\033[;35m" + "4. Aleatoria")
    print("\033[;37m")
    nivel = input("Ingrese el numero correspondiente a la dificultad:       ")
    if nivel.isnumeric():
        nivel = int(nivel)
        if nivel > 0 and nivel < 5:
            return nivel
    return bienvenida(pistas)

def elegirCategoria(opcion):
    archivos = ["facil.txt", "medio.txt", "dificil.txt", "palabras.txt"]
    conjuntoPalabras = []
    opcionArch = archivos[opcion-1]
    with open(opcionArch) as archivo:
        #El contenido del archivo seleccionado se guarda en el array diccionario
        conjuntoPalabras = archivo.read().split()
    return conjuntoPalabras

def revelarPistas(pistas,palabra,letrasUsadas):
    #Generamos un indice aleatorio para buscar una pista, solo si tiene pistas disponibles
        indAlea = random.randrange(len(palabra))
        if palabra[indAlea] not in letrasUsadas:
            letrasUsadas += palabra[indAlea]
            pistas -= 1
            return palabra[indAlea], letrasUsadas, pistas
        return revelarPistas(pistas,palabra,letrasUsadas)

def buscarPalabra(diccionario):
    #Escoge una palabra de forma aleatoria dentro del array de palabras
    return random.choice(diccionario).lower()

def tableroVisual(grafico, letraIncorrecta, letraCorrecta, palabra,pistas):
    #Muestra el tablero y progreso del jugador en pantalla
    if pistas > 0:
        print("\033[;32m")
    else:
        print("\033[;31m")
    print(f"Pistas disponibles: {pistas}")
    if pistas > 0:
        print("Si desea utilizarla escriba 'pista'")
    print("\033[;31m")
    print(grafico[len(letraIncorrecta)])
    print("\033[;37m")
    print("Letras incorrectas:  ", end='')
    for letra in letraIncorrecta:
        print(letra, end=" ")
    print("")

    espacio = '_' * len(palabra)

    for i in range(len(palabra)):
        if palabra[i] in letraCorrecta:
            espacio = espacio[:i] + palabra[i] + espacio[i+1:]

    for letra in espacio:
        print(letra, end=' ')
    print("")

def elegirLetra(letraCorrecta,letraIncorrecta,palabra,pistas):
    #Pide una letra y comprueba si la misma se encuentra disponible
    letraCualquiera = letraCorrecta + letraIncorrecta
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while(True):
        letra = input("Ingrese una letra:   ").lower()
        if (len(letra) != 1):
            if letra == "pista" and pistas > 0:
                letra, letraCorrecta, pistas = revelarPistas(pistas,palabra,letraCorrecta)
                return letra, letraCorrecta, pistas
            else:
                print("\033[;31m")
                print("Ingrese solo una letra!!")
        elif letra in letraCualquiera:
            print("\033[;31m")
            print("Ya haz probado con esta, mejor prueba con otra")
        elif letra not in abecedario:
            print("\033[;31m")
            print("Debes escoger una letra (a-z)")
        else:
            return letra, letraCorrecta, pistas

def empezar():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

def cambiarDificultad():
    print ('Quieres cambiar de dificultad? (Si o No)')
    return input().lower().startswith('s')
