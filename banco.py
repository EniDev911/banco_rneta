from validaciones import validar_rut, validar_monto, validar_tipo_y_longitud
from getpass import getpass
import pwinput # pip intall pwinput

clientes = {}

contactos = [
    {
        "nombre": "Mauro",
        "apellido": "Valdivía",
        "cuenta": "19041151"
    },
    {
        "nombre": "Marco",
        "apellido": "Contreras",
        "cuenta": "17797793"
    }
]

def registrar_cliente():
    nombre = input("Por favor ingrese su nombre: ")
    apellido = input("Por favor ingrese su apellido: ")
    # rut = getpass("RUT (XX.XXX.XXX-X): ")
    rut = pwinput.pwinput("RUT (XX.XXX.XXX-X): ", mask="*") # pip install pwinput

    if not validar_tipo_y_longitud(nombre, apellido):
        print("Datos ingresados")

    while not validar_rut(rut):
        print("Vuelve a intentar")
        rut = pwinput.pwinput("RUT (XX.XXX.XXX-X): ", mask="*")

    cuenta = rut.replace(".", "").split("-")[0]

    while True:
        deposito = input("Monto inicial de depósito: ")
        if validar_monto(deposito):
            deposito =  int(deposito)
            break
        print("Monto inválido.")

    if deposito <= 100000:
        linea = 50000
        tarjeta = 80000
    elif deposito <= 500000:
        linea = 250000
        tarjeta = 300000
    else:
        linea = 500000
        tarjeta = 700000
    
    print(f"Debido a que su primer depósito es de ${deposito}. Sus beneficios son:")
    print(f"Línea de crédito por ${linea}")
    print(f"Tarjeta de crédito por ${tarjeta}")

    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "rut": rut,
        "cuenta": cuenta,
        "saldo": deposito,
        "linea_credito": linea,
        "deuda_linea": 0,
        "tarjeta": tarjeta,
        "avance": None
    }


    print(f"Cliente {nombre} registrado. Cuenta: {cuenta}")
    return cliente

def realizar_transferencia(cliente):
    if not cliente:
        print("Debe registrar un cliente primero.")
        return

    print("Contactos:")
    for i, c in enumerate(contactos):
        print(f"{i + 1}.- {c['nombre']} {c['apellido']} --- NRO CUENTA: {c['cuenta']}")

    try:
        idx = int(input("Por favor ingrese el número correspondiente al contacto: ")) - 1
        if not (0 <= idx < len(contactos)):
            print("Contacto inválido.")
            return

        monto = float(input("Monto a transferir: "))
        total_disponible = cliente['saldo'] + (cliente['linea_credito'] - cliente['deuda_linea'])

        if monto > total_disponible:
            print("Saldo insuficiente.")
            return

        if not confirmar_autorizacion():
            print("Transferencia cancelada.")
            return

        if monto <= cliente['saldo']:
            cliente['saldo'] -= monto
        else:
            restante = monto - cliente['saldo']
            cliente['saldo'] = 0
            cliente['deuda_linea'] += restante

        print("Transferencia realizada con éxito.")
    except:
        print("Error al procesar transferencia.")


def realizar_deposito(cliente):
    if not cliente:
        print("Debe registrar un cliente primero.")
        return

    try:
        monto = float(input("Monto a depositar: "))
        if cliente['deuda_linea'] > 0:
            if monto >= cliente['deuda_linea']:
                monto -= cliente['deuda_linea']
                cliente['deuda_linea'] = 0
            else:
                cliente['deuda_linea'] -= monto
                monto = 0
        cliente['saldo'] += monto
        print("Dep\u00f3sito realizado.")
    except:
        print("Monto inv\u00e1lido.")


def solicitar_avance(cliente):
    if not cliente:
        print("Debe registrar un cliente primero.")
        return

    try:
        monto = float(input("Monto de avance: "))
        if monto > cliente['tarjeta']:
            print("Excede el límite de la tarjeta.")
            return

        print("Opciones de cuotas: 12 (1.5%), 24 (3%), 36 (4%), 48 (5%)")
        cuotas = int(input("Ingrese número de cuotas: "))

        tasas = {12: 1.5, 24: 3, 36: 4, 48: 5}
        if cuotas not in tasas:
            print("Cuotas no permitidas.")
            return

        interes = tasas[cuotas]
        cuota_mensual = (monto / cuotas) * (1 + interes / 100)

        cliente['avance'] = {
            "monto": monto,
            "cuotas": cuotas,
            "cuota_mensual": cuota_mensual,
            "abonado": 0,
            "pagadas": 0
        }

        cliente['saldo'] += monto
        print(f"Avance aprobado. Cuota mensual: ${cuota_mensual:.2f}")

    except:
        print("Datos inválidos.")


def pagar_cuota_avance(cliente):
    if not cliente or not cliente.get("avance"):
        print("No hay avance activo.")
        return

    avance = cliente['avance']
    cuota = avance['cuota_mensual']
    capital_por_cuota = avance['monto'] / avance['cuotas']
    total_disponible = cliente['saldo'] + (cliente['linea_credito'] - cliente['deuda_linea'])

    if cuota > total_disponible:
        print("Saldo insuficiente para pagar la cuota.")
        return

    # if not confirmar_autorizacion():
    #     print("Pago cancelado.")
    #     return

    if cuota <= cliente['saldo']:
        cliente['saldo'] -= cuota
    else:
        restante = cuota - cliente['saldo']
        cliente['saldo'] = 0
        cliente['deuda_linea'] += restante

    avance['abonado'] += capital_por_cuota
    avance['pagadas'] += 1
    print(f"Cuota pagada. Monto abonado: ${avance['abonado']:.2f}. Monto adeudado: ${avance['monto'] - avance['abonado']:.2f}")


def ver_resumen(cliente):
    if not cliente:
        print("Debe registrar un cliente primero.")
        return

    print("\n--- RESUMEN CLIENTE ---")
    for clave, valor in cliente.items():
        if clave != "avance":
            print(f"{clave.capitalize()}: {valor}")

    if cliente.get("avance"):
        a = cliente['avance']
        print("\nAvance activo:")
        print(f"Monto total: ${a['monto']:.2f}")
        print(f"Cuotas: {a['cuotas']} pagadas: {a['pagadas']}")
        print(f"Monto abonado: ${a['abonado']:.2f}")
        print(f"Monto adeudado: ${a['monto'] - a['abonado']:.2f}")

if __name__ == "__main__":
    registrar_cliente()