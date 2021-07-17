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

def bienvenida(booleano):
    if not booleano:
        print("A    H   O   R   C   A   D   O")
        print("Escoja su nivel de dificultad:   ")
        print("1. Facil")
        print("2. Medio")
        print("3. Dificil")
        nivel = input("Ingrese el numero correspondiente a la dificultad:       ")

diccionario = []
with open("palabras.txt") as palabras:
    #El contenido de "palabras.txt" se guarda en el array diccionario
    diccionario = palabras.read().split()

def buscarPalabra(diccionario):
    #Escoge una palabra de forma aleatoria dentro del array de palabras
    return random.choice(diccionario).lower()

def tableroVisual(grafico, letraIncorrecta, letraCorrecta, palabra):
    #Muestra el tablero y progreso del jugador en pantalla
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

def elegirLetra(letraCualquiera):
    #Pide una letra y comprueba si la misma se encuentra disponible
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    while(True):
        letra = input("Ingrese una letra:   ").lower()
        if (len(letra) != 1):
            print("Ingrese solo una letra!!")
        elif letra in letraCualquiera:
            print("Ya haz probado con esta, mejor prueba con otra")
        elif letra not in abecedario:
            print("Debes escoger una letra (a-z)")
        else:
            return letra

def empezar():
    print ('Quieres jugar de nuevo? (Si o No)')
    return input().lower().startswith('s')
