"""Gestor de Gastos Personales - aplicación de consola en Python.

Permite registrar gastos, listarlos, ver un resumen por categoría
y eliminarlos. Los datos se guardan en un archivo JSON local.
"""

import json
import os
from datetime import date

ARCHIVO = "gastos.json"
CATEGORIAS = ["Comida", "Transporte", "Estudios", "Ocio", "Otros"]


def cargar_gastos():
    """Lee los gastos del archivo JSON. Si no existe, devuelve lista vacía."""
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_gastos(gastos):
    """Guarda la lista de gastos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=2, ensure_ascii=False)


def pedir_monto():
    """Pide un monto válido (número positivo) hasta que el usuario lo escriba bien."""
    while True:
        try:
            monto = float(input("Monto: ").replace(",", "."))
            if monto > 0:
                return monto
            print("El monto debe ser mayor que 0.")
        except ValueError:
            print("Escribe un número válido.")


def elegir_categoria():
    """Muestra las categorías y devuelve la elegida."""
    print("Categorías:")
    for i, cat in enumerate(CATEGORIAS, start=1):
        print(f"  {i}. {cat}")
    while True:
        opcion = input("Elige una categoría (número): ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(CATEGORIAS):
            return CATEGORIAS[int(opcion) - 1]
        print("Opción no válida.")


def agregar_gasto(gastos):
    descripcion = input("Descripción: ").strip() or "Sin descripción"
    monto = pedir_monto()
    categoria = elegir_categoria()
    gastos.append({
        "fecha": date.today().isoformat(),
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria,
    })
    guardar_gastos(gastos)
    print("✔ Gasto registrado.")


def listar_gastos(gastos):
    if not gastos:
        print("Todavía no hay gastos registrados.")
        return
    print(f"\n{'#':<4}{'Fecha':<12}{'Categoría':<12}{'Monto':>10}  Descripción")
    print("-" * 60)
    for i, g in enumerate(gastos, start=1):
        print(f"{i:<4}{g['fecha']:<12}{g['categoria']:<12}{g['monto']:>10.2f}  {g['descripcion']}")


def resumen(gastos):
    if not gastos:
        print("No hay datos para resumir.")
        return
    totales = {}
    for g in gastos:
        totales[g["categoria"]] = totales.get(g["categoria"], 0) + g["monto"]
    total = sum(totales.values())
    print("\nResumen por categoría")
    print("-" * 35)
    for cat, valor in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat:<12}{valor:>10.2f}  ({valor / total * 100:.1f}%)")
    print("-" * 35)
    print(f"{'TOTAL':<12}{total:>10.2f}")


def eliminar_gasto(gastos):
    listar_gastos(gastos)
    if not gastos:
        return
    numero = input("Número del gasto a eliminar: ")
    if numero.isdigit() and 1 <= int(numero) <= len(gastos):
        eliminado = gastos.pop(int(numero) - 1)
        guardar_gastos(gastos)
        print(f"✔ Eliminado: {eliminado['descripcion']}")
    else:
        print("Número no válido.")


def menu():
    gastos = cargar_gastos()
    while True:
        print("\n=== GESTOR DE GASTOS ===")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Resumen por categoría")
        print("4. Eliminar gasto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            listar_gastos(gastos)
        elif opcion == "3":
            resumen(gastos)
        elif opcion == "4":
            eliminar_gasto(gastos)
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
