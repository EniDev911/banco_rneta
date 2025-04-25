ANCHO = 40

def encabezado(titulo, emoji=""):
    Y = "+" + ("=" * ANCHO) + "+"
    if emoji:
        aux = len(emoji.split(" "))
        X = u"|" + f"{emoji} {titulo} {emoji}".upper().center(ANCHO - aux * 2) + "|"
    else:
        X = "|" + titulo.upper().center(ANCHO) + "|"
                             
    return "\n".join([Y,X,Y])
