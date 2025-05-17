import json
from datetime import datetime

opcion = 0

def guardar_tarea(tarea):
    with open("Datos.json", "w", encoding="utf-8") as archivo:
        json.dump(tarea, archivo, indent=4, sort_keys=True, ensure_ascii=False)

def mostrar_agenda():
    with open("Datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
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
        
        titulo = input("Ingrese un Titulo \n").title()
        descripcion = input("Ingrese la descripcion \n").title()
        fecha = input("ingrese la fecha limite (formato DD-MM-YYYY) \n")
        agenda_archivo = mostrar_agenda()
        agenda_archivo[titulo] = {
            "Descripcion": descripcion,
            "Fecha Limite": fecha,
            "Estado":"Pendiente"
        }
        guardar_tarea(agenda_archivo)

    elif opcion == "2":
        agenda_archivo = mostrar_agenda()
        tarea_modificar = input("Ingrese el Titulo de la tarea que desea completar: \n").title()
        if tarea_modificar in agenda_archivo:
            agenda_archivo[tarea_modificar].update({"Estado": "Completado"})
            agenda_archivo[tarea_modificar]["Fecha tarea completada"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Se completo la tarea {tarea_modificar}, Descripcion: {agenda_archivo[tarea_modificar]["Descripcion"]},
                   Fecha Limite: {agenda_archivo[tarea_modificar]["Fecha Limite"]}, 
                   Estado:{agenda_archivo[tarea_modificar]["Estado"]},  
                   La tarea se completo con fecha:{agenda_archivo[tarea_modificar]["Fecha tarea completada"]}\n")
            guardar_tarea(agenda_archivo)
        else:
            print("La tarea no se encuentra en la Agenda")

    elif opcion == "3":
        agenda_archivo = mostrar_agenda()
        tarea_eliminar = input("Ingrese el Titulo de la tarea que desea eliminar: \n").title()
        if tarea_eliminar in agenda_archivo:
            valor = agenda_archivo.pop(tarea_eliminar)
            print(f"Se elimino la tarea {tarea_eliminar},\n Descripcion: {valor["Descripcion"]},\n Fecha Limite: {valor["Fecha Limite"]},\n Estado:{valor["Estado"]}\n")
            guardar_tarea(agenda_archivo)
        else:
            print("La tarea no se encuentra en la Agenda")

    elif opcion == "4":
        agenda_archivo = mostrar_agenda()

        print("TAREAS COMPLETADAS")
        for nombre_tarea in agenda_archivo:
            if agenda_archivo[nombre_tarea]["Estado"] == "Completado":
                print(f"\n {nombre_tarea}")
                for clave, valor in agenda_archivo[nombre_tarea].items():
                    print(f"{clave}: {valor}")

        print("\nTAREAS PENDIENTES")
        for nombre_tarea in agenda_archivo:
            if agenda_archivo[nombre_tarea]["Estado"] == "Pendiente":
                print(f"\n {nombre_tarea}")
                for clave, valor in agenda_archivo[nombre_tarea].items():
                    print(f"{clave}: {valor}")
            
                


