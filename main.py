from funcion import *

def main():
    pistas = 0
    nivel = bienvenida(pistas)
    diccionario = elegirCategoria(nivel)
    letraCorrecta = ""
    letraIncorrecta = ""
    palabra = buscarPalabra(diccionario)
    fin = False

    while (True):
        os.system('clear')
        tableroVisual(graficos,letraIncorrecta,letraCorrecta,palabra,pistas)
        letra, letraCorrecta, pistas = elegirLetra(letraCorrecta,letraIncorrecta,palabra,pistas)

        if letra in palabra:
            #Comprueba si la letra ingresada se encuentra dentro de la palabra
            # y lo agrega a todas las letras encontradas
            letraCorrecta += letra
            letrasEncontradas = True
            for i in range(len(palabra)):
                if(palabra[i] not in letraCorrecta):
                    letrasEncontradas = False
                    break
            if (letrasEncontradas):
                #El juego finaliza si la palabra ha sido encontrada
                print("\033[;32m"+f"Genial! La palabra secreta es: {palabra}    ")
                print("Haz ganado!!")
                pistas += 1
                fin = True
        else:
            #Si la letra es erronea lo agrega a las letra equivocadas
            letraIncorrecta += letra
            if(len(letraIncorrecta) == len(graficos)-1):
                #Finaliza el juego si ya no quedan mas intentos
                os.system('clear')
                tableroVisual(graficos,letraIncorrecta,letraCorrecta,palabra,pistas)
                print("\033[;31m"+"Se ha quedado sin vidas :(")
                print(f"Tuviste {len(letraIncorrecta)} errores y {len(letraCorrecta)} aciertos.")
                print(f"La palabra oculta era:  {palabra}")
                fin = True
        if fin:
            if empezar():
                #Si el jugador asi lo desea el juego vuelve a comenzar con una nueva palabra y preguntamos si desea cambiar de dificultad
                if cambiarDificultad():
                    nivel = bienvenida(pistas)
                    diccionario = elegirCategoria(nivel)
                    letraCorrecta = ""
                    letraIncorrecta = ""
                    palabra = buscarPalabra(diccionario)
                    fin = False
                else:
                    letraIncorrecta = ""
                    letraCorrecta = ""
                    fin = False
                    palabra = buscarPalabra(diccionario)
            else:
                os.system('clear')
                break


if __name__ == '__main__':
    main()
