# Mesa de Partes Digital - Huayco
# Proyecto académico de Fundamentos de Programación
import json
from pathlib import Path

ARCHIVO_DATOS = Path("expedientes.json")
ESTADOS = ("Pendiente", "En proceso", "Atendido")


def cargar_expedientes():
    """Lee los expedientes guardados. Si no existe el archivo, empieza vacío."""
    if not ARCHIVO_DATOS.exists():
        return []
    try:
        with ARCHIVO_DATOS.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if isinstance(datos, list):
            return datos
        print("Advertencia: el archivo no tiene el formato esperado.")
    except (json.JSONDecodeError, OSError) as error:
        print(f"Advertencia: no se pudo leer el archivo: {error}")
    return []


def guardar_expedientes(expedientes):
    """Guarda los expedientes en un archivo JSON."""
    temporal = ARCHIVO_DATOS.with_suffix(".json.tmp")
    with temporal.open("w", encoding="utf-8") as archivo:
        json.dump(expedientes, archivo, ensure_ascii=False, indent=4)
    temporal.replace(ARCHIVO_DATOS)


def siguiente_codigo(expedientes):
    """Crea códigos consecutivos como EXP-0001."""
    mayor = 0
    for expediente in expedientes:
        codigo = expediente.get("codigo", "")
        if codigo.startswith("EXP-"):
            try:
                mayor = max(mayor, int(codigo[4:]))
            except ValueError:
                pass
    return f"EXP-{mayor + 1:04d}"


def pedir_obligatorio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo es obligatorio. Intente nuevamente.")


def registrar_reporte(expedientes):
    print("\n--- Registrar reporte ciudadano ---")
    nombre = pedir_obligatorio("Nombre del ciudadano: ")
    documento = pedir_obligatorio("DNI u otro documento: ")
    telefono = pedir_obligatorio("Teléfono de contacto: ")
    ubicacion = pedir_obligatorio("Ubicación del huaico o deslizamiento: ")
    descripcion = pedir_obligatorio("Descripción del incidente: ")

    expediente = {
        "codigo": siguiente_codigo(expedientes),
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono,
        "ubicacion": ubicacion,
        "descripcion": descripcion,
        "estado": "Pendiente",
    }
    expedientes.append(expediente)
    guardar_expedientes(expedientes)
    print(f"\nReporte registrado correctamente. Código: {expediente['codigo']}")


def buscar_expediente(expedientes):
    print("\n--- Buscar expediente ---")
    codigo = pedir_obligatorio("Ingrese el código (por ejemplo, EXP-0001): ").upper()
    expediente = next(
        (e for e in expedientes if e.get("codigo", "").upper() == codigo), None
    )
    if expediente:
        mostrar_expediente(expediente)
    else:
        print("No se encontró un expediente con ese código.")


def mostrar_expediente(expediente):
    print("\n" + "-" * 40)
    print(f"Código:      {expediente.get('codigo', '')}")
    print(f"Ciudadano:   {expediente.get('nombre', '')}")
    print(f"Documento:   {expediente.get('documento', '')}")
    print(f"Teléfono:    {expediente.get('telefono', '')}")
    print(f"Ubicación:   {expediente.get('ubicacion', '')}")
    print(f"Descripción: {expediente.get('descripcion', '')}")
    print(f"Estado:      {expediente.get('estado', 'Pendiente')}")
    print("-" * 40)


def listar_expedientes(expedientes):
    print("\n--- Expedientes registrados ---")
    if not expedientes:
        print("Todavía no hay reportes registrados.")
        return
    for expediente in sorted(expedientes, key=lambda e: e.get("codigo", "")):
        mostrar_expediente(expediente)


def actualizar_estado(expedientes):
    print("\n--- Actualizar estado ---")
    codigo = pedir_obligatorio("Código del expediente: ").upper()
    expediente = next(
        (e for e in expedientes if e.get("codigo", "").upper() == codigo), None
    )
    if not expediente:
        print("No se encontró un expediente con ese código.")
        return

    print("Seleccione el nuevo estado:")
    for numero, estado in enumerate(ESTADOS, start=1):
        print(f"{numero}. {estado}")
    while True:
        opcion = input("Opción (1-3): ").strip()
        if opcion in ("1", "2", "3"):
            break
        print("Opción no válida. Escriba 1, 2 o 3.")

    expediente["estado"] = ESTADOS[int(opcion) - 1]
    guardar_expedientes(expedientes)
    print(f"Estado actualizado: {codigo} -> {expediente['estado']}")


def menu():
    expedientes = cargar_expedientes()
    while True:
        print("\n====================================")
        print("   MESA DE PARTES DIGITAL - HUAYCO")
        print("====================================")
        print("1. Registrar reporte")
        print("2. Buscar expediente por código")
        print("3. Mostrar todos los expedientes")
        print("4. Actualizar estado")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_reporte(expedientes)
        elif opcion == "2":
            buscar_expediente(expedientes)
        elif opcion == "3":
            listar_expedientes(expedientes)
        elif opcion == "4":
            actualizar_estado(expedientes)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Seleccione del 1 al 5.")


if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
