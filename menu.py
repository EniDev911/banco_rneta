from utilidades import encabezado

def menu_principal():
    print(encabezado("Banco rneta", "\U0001F3E6") + "\n")
    print("1. Registrar cliente")
    print("0. Salir")

def sub_menu():
    print("1. Realizar transferencia")
    print("2. Realizar depósito")
    print("3. Solicitar avance con tarjeta de crédito")
    print("4. Pagar cuota de avance")
    print("5. Ver resumen")

def menu_bienvenida(cliente):
    print(encabezado("BANCO RNETA", "\U0001F3E6"))
    print(f"\nNRO. CUENTA: {cliente['cuenta']}\n\n")
    print(f"Saldo: ${cliente['saldo']}")
    print(f"Línea de crédito: ${cliente['linea_credito']}")
    print(f"Tarjeta de crédito: ${cliente['tarjeta']}")


if __name__ == "__main__":
    menu_principal()