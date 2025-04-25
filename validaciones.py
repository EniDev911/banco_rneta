def validar_rut(rut:str) -> bool:
    try:
        rut = rut.replace(".", "")
        rut = rut.replace(",", "")
        if len(rut) >= 8 and len(rut) <= 12:
            posicion_guion = rut[-2]
            if posicion_guion == "-":
                partes = rut.split("-")
                cuerpo_rut = partes[0]
                dv = partes[1]
                revertido = list(map(int, reversed(str(cuerpo_rut))))
                factores = [2, 3, 4, 5, 6, 7]
                suma = 0
                for i, d in enumerate(revertido):
                    factor = factores[i % len(factores)]
                    suma +=  d * factor
                res = (-suma) % 11
                if str(res) == dv:
                    return True
                elif dv == "k" and str(res) == 10:
                    return True
                else:
                    print("El RUN no es válido")
                    return False
            else:
                print("El formato del RUN debe contener el guión antes del dígito verificador")
                return False
        else:
            return False

    except ValueError as e:
        print("El valor ingresado no es válido")
        return False
    except AttributeError as e:
        print("El valor ingresado debe ser una cadena de texto para evaluar")
        return False

def validar_tipo_y_longitud(*args: str) -> bool:
    es_valido = {}

    for elemento in args:
        es_valido[elemento] = type(elemento) == str and len(elemento) >= 3
    
    return all(es_valido.values())

def validar_monto(monto):
    try:
        monto = int(monto)
        return monto > 0
    except ValueError as e:
        print(f"El monto '{monto}' ingresado no es válido: ", e)
        return False

def validar_opcion(opcion, opciones):
    return True if opcion in opciones else False

if __name__ == "__main__":
    validar_rut("17.797.793-3")





    