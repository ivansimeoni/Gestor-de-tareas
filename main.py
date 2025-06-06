import json
from datetime import datetime

opcion = 0

# Declaro variables globales 
ESTADO_PENDIENTE = "Pendiente"
ESTADO_COMPLETADO = "Completado"

# Función para guardar tareas en el archivo JSON
def guardar_tarea(tarea):
    with open("Datos.json", "w", encoding="utf-8") as archivo:
        json.dump(tarea, archivo, indent=4, sort_keys=True, ensure_ascii=False)

# Función para leer tareas del archivo JSON
def mostrar_agenda():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print("El archivo no existe. Primero tiene que agregar tareas")
        return {}


# Bucle acentos  
while opcion != "fin":
    # Muestra grilla de opciones al usuario 
    opcion = input("""Indique cual de las siguientes tareas desea realizar:\n
                \t 1.- Añadir tarea nueva \n
                \t 2.- Completar una tarea \n
                \t 3.- Eliminar una tarea \n
                \t 4.- Ver lista de tareas \n
                Para finalizar ingrese 'Fin' \n
                """).lower()
    
    # Solicita los datos para agregar una nueva tarea 
    if opcion == "1":
        
        titulo = input("Ingrese un Titulo \n").title()
        descripcion = input("Ingrese la descripcion \n").title()
        fecha = input("ingrese la fecha limite (formato DD-MM-YYYY) \n")
        agenda_archivo = mostrar_agenda()
        agenda_archivo[titulo] = {
            "Descripcion": descripcion,
            "Fecha Limite": fecha,
            "Estado":ESTADO_PENDIENTE
        }
        guardar_tarea(agenda_archivo)

    # Solicita al usuario la tarea para modificar el estado a "Completado", añade la fecha en la que se completo la tarea
    elif opcion == "2":
        agenda_archivo = mostrar_agenda()
        tarea_modificar = input("Ingrese el Titulo de la tarea que desea completar: \n").title()
        if tarea_modificar in agenda_archivo:
            agenda_archivo[tarea_modificar].update({"Estado": ESTADO_COMPLETADO})
            agenda_archivo[tarea_modificar]["Fecha tarea completada"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"""Se completo la tarea {tarea_modificar}, 
                  Descripcion: {agenda_archivo[tarea_modificar]["Descripcion"]}, 
                  Fecha Limite: {agenda_archivo[tarea_modificar]["Fecha Limite"]}, 
                  Estado:{agenda_archivo[tarea_modificar]["Estado"]},  
                  La tarea se completo con fecha:{agenda_archivo[tarea_modificar]["Fecha tarea completada"]}\n""")
            guardar_tarea(agenda_archivo)
        else:
            print("La tarea no se encuentra en la Agenda")

    # Solicita al usuario la tarea para eliminar
    elif opcion == "3":
        agenda_archivo = mostrar_agenda()
        tarea_eliminar = input("Ingrese el Titulo de la tarea que desea eliminar: \n").title()
        if tarea_eliminar in agenda_archivo:
            valor = agenda_archivo.pop(tarea_eliminar)
            print(f"Se elimino la tarea {tarea_eliminar},\n Descripcion: {valor['Descripcion']},\n Fecha Limite: {valor['Fecha Limite']},\n Estado:{valor['Estado']}\n")
            guardar_tarea(agenda_archivo)
        else:
            print("La tarea no se encuentra en la Agenda")

    # Lista todas las tareas "completas" primero y después todas las tareas "pendientes"
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
            if agenda_archivo[nombre_tarea]["Estado"] == ESTADO_PENDIENTE:
                print(f"\n {nombre_tarea}")
                for clave, valor in agenda_archivo[nombre_tarea].items():
                    print(f"{clave}: {valor}")
            
    # Si el usuario ingresa "fin" se sale del bucle
    elif opcion == "fin":
        print("Gracias por usar la agenda")