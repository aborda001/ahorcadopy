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
    print(f"A    H   O   R   C   A   D   O       {pistas} pistas")
    print(graficos[6])
    print("Escoja su nivel de dificultad:   ")
    print("1. Facil")
    print("2. Medio")
    print("3. Dificil")
    print("4. Aleatoria")
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
    print(f"Tiene {pistas} pistas disponible")
    if pistas > 0:
        print("Si desea utilizarla escriba 'pista'")
    print(grafico[len(letraIncorrecta)])
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
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    while(True):
        letra = input("Ingrese una letra:   ").lower()
        if (len(letra) != 1):
            if letra == "pista" and pistas > 0:
                letra, letraCorrecta, pistas = revelarPistas(pistas,palabra,letraCorrecta)
                return letra, letraCorrecta, pistas
            else:
                print("Ingrese solo una letra!!")
        elif letra in letraCualquiera:
            print("Ya haz probado con esta, mejor prueba con otra")
        elif letra not in abecedario:
            print("Debes escoger una letra (a-z)")
        else:
            return letra, letraCorrecta, pistas

def empezar():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')

def cambiarDificultad():
    print ('Quieres cambiar de dificultad? (Si o No)')
    return input().lower().startswith('s')
