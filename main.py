import json
from datetime import datetime

opcion = 0
#agenda= {}
agenda = {
    "Tarea 1": {
        "Descripcion": "Revisar informe financiero.",
        "Fecha Limite": "2025-06-01",
        "Estado": "Pendiente"
    },
    "Tarea 2": {
        "Descripcion": "Preparar presentación para reunión de equipo.",
        "Fecha Limite": "2025-05-15",
        "Estado": "Pendiente"
    },
    "Tarea 3": {
        "Descripcion": "Revisar correos electrónicos importantes.",
        "Fecha Limite": "2025-05-10",
        "Estado": "Pendiente"
    },
    "Tarea 4": {
        "Descripcion": "Actualizar el sitio web de la empresa.",
        "Fecha Limite": "2025-06-05",
        "Estado": "Pendiente"
    },
    "Tarea 5": {
        "Descripcion": "Llamar a proveedores para confirmar fechas.",
        "Fecha Limite": "2025-05-20",
        "Estado": "Pendiente"
    },
    "Tarea 6": {
        "Descripcion": "Organizar el archivo de proyectos.",
        "Fecha Limite": "2025-05-25",
        "Estado": "Pendiente"
    },
    "Tarea 7": {
        "Descripcion": "Enviar presupuesto a cliente X.",
        "Fecha Limite": "2025-05-18",
        "Estado": "Pendiente"
    },
    "Tarea 8": {
        "Descripcion": "Programar cita con equipo de marketing.",
        "Fecha Limite": "2025-05-12",
        "Estado": "Pendiente"
    },
    "Tarea 9": {
        "Descripcion": "Escribir artículo para blog.",
        "Fecha Limite": "2025-06-01",
        "Estado": "Pendiente"
    },
    "Tarea 10": {
        "Descripcion": "Hacer seguimiento de pagos pendientes.",
        "Fecha Limite": "2025-05-30",
        "Estado": "Completado"
    }
}
"""
write = json.dump()
read = json.load()
update = json.update()
"""
def guardar_tarea(tarea):
    with open("Datos.json", "w", encoding="utf-8") as archivo:
        json.dump(tarea, archivo, indent=4, ensure_ascii=False)


def eliminar_tarea(tarea):
    json.update()
    pass

def mostrar_agenda():
    with open("Datos.json", "r", encoding="utf-8") as agenda_archivo:
        datos = json.load(agenda_archivo)
    return datos



while opcion != "fin":

    opcion = input("""Indique cual de las siguientes tareas desea realizar:\n
                \t 1.- Añadir tarea nueva \n
                \t 2.- Completar una tarea \n
                \t 3.- Eliminar una tarea \n
                \t 4.- Ver lista de tareas \n
                Para finalizar ingrese 'Fin' \n
                """).lower()

    if opcion == "1":

        titulo = input("Ingrese un Titulo \n")
        descripcion = input("Ingrese la descripcion \n")
        fecha = input("ingrese la fecha limite \n")

        agenda[titulo] = {
            "Descripcion": descripcion,
            "Fecha Limite": fecha,
            "Estado":"Pendiente"
        }
        guardar_tarea(agenda)

    elif opcion == "2":
        tarea_modificar = input("Ingrese el Titulo de la tarea que desea completar: \n").title()
        agenda[tarea_modificar].update({"Estado": "Completado"})
        print(agenda[tarea_modificar])

    elif opcion == "3":
        tarea_eliminar = input("Ingrese el Titulo de la tarea que desea eliminar: \n").title()
        valor = agenda.pop(tarea_eliminar)
        print(f"Se elimino la tarea {tarea_eliminar}, {valor}")

    elif opcion == "4":
        agenda_desde_archivo = mostrar_agenda()

        print("TAREAS COMPLETADAS")
        for nombre_tarea in agenda_desde_archivo:
            if agenda_desde_archivo[nombre_tarea]["Estado"] == "Completado":
                print(f"\n {nombre_tarea}")
                for clave, valor in agenda_desde_archivo[nombre_tarea].items():
                    print(f"{clave}: {valor}")

        print("\nTAREAS PENDIENTES")
        for nombre_tarea in agenda_desde_archivo:
            if agenda_desde_archivo[nombre_tarea]["Estado"] == "Pendiente":
                print(f"\n {nombre_tarea}")
                for clave, valor in agenda_desde_archivo[nombre_tarea].items():
                    print(f"{clave}: {valor}")
            
                


