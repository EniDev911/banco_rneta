from menu import menu_principal, menu_bienvenida, sub_menu
from banco import registrar_cliente
from utilidades import encabezado, limpiar_pantalla
from validaciones import validar_opcion
import os, time

def main():
    limpiar_pantalla()
    while True:
        menu_principal()
        opcion = input("Selecciona:> ")

        if validar_opcion(opcion, ["1", "0"]):
            if opcion == "1":
                limpiar_pantalla()
                print(encabezado("REGISTRO NUEVO CLIENTE","\U0001F3E6"))
                cliente = registrar_cliente()
                time.sleep(5)
                limpiar_pantalla()
                menu_bienvenida(cliente)
                while True:
                    sub_menu()
                    opcion = input("Selecciona:> ")
                    if validar_opcion(opcion, ["1", "2", "3", "4"]):
                        pass
                break
            elif opcion == "0":
                break
        else:
            limpiar_pantalla()
            print("Opción no válida")

    os._exit(1)

if __name__ == "__main__":
    main()
