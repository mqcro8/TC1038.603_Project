"""
Miguel Ceballos Aguilar

Enlace a cuenta de GitHub: https://github.com/mqcro8

Enlace a repo: https://github.com/mqcro8/TC1038.603_Project
"""

def add_task():

    # Se solicitan los datos necesarios para crear una tarea nueva
    tarea = input("\n¿Cuál es el nombre de la tarea?\n> ")
    fecha_limit = input("¿Cuándo es la fecha límite?\n> ")
    descripcion = input("Describe la tarea\n> ")
    completada = False

    # Se guarda la información en una lista y se añade a la lista de tareas
    nueva_tarea = [tarea, fecha_limit, descripcion, completada]

    print("\nTarea añadida a la bandeja de pendientes (simulación)\n")

    return nueva_tarea


def print_task(tarea, to_print):
    # Se imprime el numero de la tarea
    print("\nTarea #", to_print)

    # Se imprime el nombre de la tarea
    print("Nombre:", tarea[0])

    # Se imprime la fehca limite de la tarea
    print("Fecha límite:", tarea[1])

    # Se imprime la descripcion de la tarea
    print("Descripción:", tarea[2])

    # Se imprime el estado de la tarea completada/incompleta
    if tarea[3]:
        print("Estado: Completada\n")
    else:
        print("Estado: Incompleta\n")

    input("Presiona *Enter* para continuar\n>")


def get_tarea_valida(task_list):
    # Se comprueba que el usuario introduzca un número correspondiente
    while True:
        num = input("¿Qué tarea? (1-" + str(len(task_list)) + ")\n> ")

        if num.isdigit():
            num = int(num)
            
            if 1 <= num <= len(task_list):
                return num

        print("\nSolo hay", len(task_list), "tarea(s) en la lista. Intenta de nuevo.\n")

def buscar_tareas(task_list):
    # Se buscan tareas por nombre o descripción
    # split() permite buscar usando varias palabras.
    busqueda = input("¿Qué tarea buscas? (puedes buscar por nombre o descripcion)\n> ").lower()
    palabras = busqueda.split()

    if len(palabras) == 0:
        print("\nEscribe algo para buscar.\n")
        return

    encontrados = 0

    print("Resultados de búsqueda:\n")

    # Se revisan todas las tareas y se comprueba si contienen las palabras clave
    for i, tarea in enumerate(task_list):
        texto = (tarea[0] + " " + tarea[2]).lower()

        coincide = True

        for palabra in palabras:
            if palabra not in texto:
                coincide = False

        if coincide:
            estado = "Completada" if tarea[3] else "Incompleta"

            print("Tarea", i + 1, ".-", tarea[0], "| Estado:", estado)
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron tareas con esas palabras.\n")

    input("\nPresiona *Enter* para continuar\n>")

def print_tasks(task_list):
    """
    Imprime todas las tareas guardadas y permite leer, completar,
    eliminar o buscar tareas.
    """

    if len(task_list) > 0:
        while True:
            print("\nImpresión de tareas (simulación):\n")

            for i, tarea in enumerate(task_list):
                if tarea[3]:
                    estado = "Completada"
                else:
                    estado = "Incompleta"

                print("Tarea", i + 1, ".-", tarea[0],
                      "| Estado:", estado)

            print("\nAquí se imprimen todas las tareas\n")

            opt = input("¿Quisieras:\n1. Leer alguna tarea completa\n2. Marcar alguna tarea como completada\n3. Eliminar una tarea\n4. Buscar una tarea\n5. Volver al menú principal\n> ")

            match(opt):
                case "1":
                    to_print = get_tarea_valida(task_list)
                    # Se resta 1 porque se inicia a contar desde 0
                    print_task(task_list[to_print - 1], to_print)

                    # Pendiente, imprimir la tarea número *to_print* de la lista de tareas
                case "2":
                    to_mark = get_tarea_valida(task_list)

                    # Se modifica el estado de la tarea seleccionada
                    task_list[to_mark - 1][3] = True

                    print("\nSe marca la tarea", to_mark,"como completada\n")
                    input("Presiona *Enter* para continuar\n>")

                case "3":
                    to_del = get_tarea_valida(task_list)

                    # Se elimina la tarea seleccionada de la lista
                    tarea_eliminada = task_list.pop(to_del - 1)

                    print("\nSe eliminó la tarea:", tarea_eliminada[0], "\n")

                    if(task_list == 0):
                        input("Ya no quedan mas tareas.\nAl menu principal\nPresiona *Enter* para continuar\n>")
                        print("")
                        break

                    # Pendiente, eliminar la tarea número *to_del*
                case "4":
                    buscar_tareas(task_list)
                case "5":
                    print("\nVolviendo al menú principal\n")
                    break
                case _:
                    # Caso por defecto cuando el usuario no elige una opción válida
                    print("\nOpción inválida... ¡Intenta de nuevo!\n")
    else:
        print("\nNo hay tareas en la lista de tareas... ¡Añade una!\n")

    # Se regresa la lista actualizada
    return task_list


def menu(task_list):
    while True:
        # Se le pregunta al usuario qué acción quiere realizar
        # El programa correrá hasta que el usuario salga
        opt = input("Escoge una opción\n1. Ver tareas\n2. Añadir tarea\n3. Salir\n> ")

        match(opt):
            case "1":
                # Se llama a la función que imprime todas las tareas
                task_list = print_tasks(task_list)
            case "2":
                # Se llama a la función que añade una tarea nueva
                task_list.append(add_task())
            case "3":
                # Se imprime un mensaje y se regresa a main para terminar el programa
                print("Saliendo del programa...")
                break
            case _:
                # Caso por defecto cuando el usuario no elige una opción válida
                print("Opción inválida... ¡Intenta de nuevo!\n")


def main():
    # La lista comienza vacía y almacena todas las tareas del usuario
    task_list = []
    print("Se crea la lista de tareas vacía\n")

    # Se pasa el contador a *menu*, ya que las funciones lo utilizarán
    menu(task_list)


if __name__ == "__main__":
    main()