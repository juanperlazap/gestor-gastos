# 💰 Gestor de Gastos Personales

Aplicación de consola hecha en **Python** que permite llevar el control de los gastos del día a día: registrarlos, consultarlos, ver cuánto se gasta por categoría y eliminarlos.

## ¿Por qué esta aplicación?

Quise resolver un problema cotidiano: saber en qué se me va el dinero. La app es deliberadamente sencilla (un solo archivo, sin dependencias) para que sea fácil de entender y de ejecutar.

## Requisitos

- Python 3.8 o superior (no necesita instalar ninguna librería).

## Cómo ejecutarla

```bash
git clone https://github.com/juanperlazap-alt/gestor-gastos.git
cd gestor-gastos
python gastos.py
```

> En algunos sistemas el comando es `python3 gastos.py`.

## Funcionamiento

Al iniciar aparece un menú:

| Opción | Qué hace |
|--------|----------|
| 1. Agregar gasto | Pide descripción, monto y categoría. La fecha se guarda automáticamente (hoy). |
| 2. Ver gastos | Muestra una tabla con todos los gastos registrados. |
| 3. Resumen por categoría | Calcula el total gastado por categoría, con su porcentaje, y el total general. |
| 4. Eliminar gasto | Muestra la lista y elimina el gasto cuyo número se indique. |
| 5. Salir | Cierra el programa. |

**Categorías disponibles:** Comida, Transporte, Estudios, Ocio, Otros.

### Ejemplo de uso

```
=== GESTOR DE GASTOS ===
1. Agregar gasto
...
Elige una opción: 1
Descripción: Almuerzo
Monto: 12000
Categoría: 1
✔ Gasto registrado.
```

Resumen:

```
Resumen por categoría
-----------------------------------
Comida        12000.00  (66.7%)
Transporte     6000.00  (33.3%)
-----------------------------------
TOTAL         18000.00
```

## Almacenamiento de datos

Los gastos se guardan automáticamente en un archivo `gastos.json` en la misma carpeta. Si el archivo no existe, se crea la primera vez que se registra un gasto. Este archivo está en `.gitignore` para no subir datos personales al repositorio.

## Estructura del proyecto

```
gestor-gastos/
├── gastos.py     # Código de la aplicación
├── README.md     # Este documento
└── .gitignore    # Archivos que Git debe ignorar
```

## Ideas para mejorar

- Filtrar gastos por mes.
- Exportar a CSV.
- Establecer un presupuesto mensual con alertas.

## Autor

Proyecto académico realizado por JUAN.
