## Gestor de tareas en consola
Este es un proyecto en Python que permita al usuario gestionar sus tareas pendientes desde la terminal. 
Las tareas se almacenan en un archivo JSON para conservarse entre ejecuciones.

---

## Características
- El programa permite:
  1. **Agregar tareas** con título, descripción y fecha límite.
  2. **Marcar tareas como completadas** registrando automáticamente la fecha de finalización.
  3. **Eliminar tareas** por título.
  4. **Listar tareas**, separando pendientes y completadas.
-**Guardar automáticamente** los cambios en un archivo `Datos.json`.

---

## Requisitos
- Python 3.x 
- Módulos:
  - `json` para almacenamiento de datos
  - `datetime` para registrar fechas
  - `os` para verificar existencia del archivo
Todos estos módulos vienen incluidos por defecto con Python, **no necesitás instalar paquetes externos**.

---

## Instrucciones de Uso
- Clona este repositorio en tu máquina local:
    ```bash 
    git clone https://github.com/ivansimeoni/Gestor-de-tareas.git
    ```
    Navega al directorio del proyecto:
    ```bash 
    cd "Gestor de tareas"
    ```
    Ejecuta el script:
    ```bash 
    python main.py
    ```

- Sigue las instrucciones que aparecen en pantalla para gestionar tus tareas:

---

## Ejemplo: agregar una tarea
- Agregar un titulo (funciona como clave única, por lo que no puede repetirse).
- Agregar la descripción.
- Indicar la fecha limite, con el siguiente formato:
    ```css 
    DD-MM-YYYY
    ```

Si no existe el archivo `Datos.json`, se crea automáticamente al agregar la primera tarea.

---

## Mejoras futuras
- Incorporar manejo de errores para entradas inválidas.
- Agregar la opción de editar tareas existentes.
- Mejorar el diseño visual en consola.

---

## Autor
ivansimeoni