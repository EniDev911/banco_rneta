ANCHO = 40
import os

def encabezado(titulo, emoji=""):
    Y = "+" + ("=" * ANCHO) + "+"
    if emoji:
        aux = len(emoji.split(" "))
        X = u"|" + f"{emoji} {titulo} {emoji}".upper().center(ANCHO - aux * 2) + "|"
    else:
        X = "|" + titulo.upper().center(ANCHO) + "|"
                             
    return "\n".join([Y,X,Y])

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")