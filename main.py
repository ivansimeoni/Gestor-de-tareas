from datetime import datetime

opcion = 0
agenda= {}

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
            "Estado":"Pedndiente"
        }

    if opcion == "2":
        tarea = input("Ingrese el Titulo de la tarea que desea completar: \n")
        agenda[tarea].update({"Estado": "Completado"})
        print(agenda)





