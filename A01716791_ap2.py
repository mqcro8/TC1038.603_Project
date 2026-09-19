def add_task():

    # Se solicitan los datos necesarios para la tarea (por ahora solo se piden)
    tarea = input("\n¿Cuál es el nombre de la tarea?\n> ")
    fecha_limit = input("¿Cuándo es la fecha límite?\n> ")
    descripcion = input("Describe la tarea\n> ")
    completada = False

    # Pendiente, guardar la tarea con los datos anteriores en la lista de tareas
    print("\nTarea añadida a la bandeja de pendientes (simulación)\n")

    # Se regresa 1 para que el menú aumente el contador de tareas
    return 1


def print_task(task_list, to_print):
    # Como todavía no se guardan tareas reales, solo se muestra un ejemplo
    # de lo que se imprimiría para la tarea número *to_print*
    print("\nTarea #", to_print)

    # Se imprimiría el nombre de la tarea *to_print* de la lista de tareas
    print("Nombre: Actividad 4 de cálculo")

    # Se imprimiría la fecha límite de la tarea *to_print* de la lista de tareas
    print("Fecha límite: 08 de Noviembre de 2026")

    # Se imprimiría la descripción de la tarea *to_print* de la lista de tareas
    print("Descripción: Realizar los ejercicios del libro de texto de la página 23-25")

    # Se imprimiría el estado de la tarea *to_print* de la lista de tareas
    print("Estado: Completada\n")

    input("Presiona *Enter* para continuar\n>")


def get_tarea_valida(task_list):
    # Pide el número de tarea y comprueba que esté entre 1 y *task_list*;
    # si no, se le avisa al usuario cuántas tareas hay y se vuelve a preguntar
    while True:
        num = int(input("¿Qué tarea? (1-" + str(task_list) + ")\n> "))

        if 1 <= num <= task_list:
            return num

        print("\nSolo hay", task_list, "tarea(s) en la lista. Intenta de nuevo.\n")


def print_tasks(task_list):
    """
        Como todavía no se guardan tareas reales, esta función simula la
        impresión de todas las tareas. Si el contador *task_list* es 0
        (aún no se ha añadido ninguna tarea), se le avisa al usuario.

        En un próximo avance, *task_list* será una lista de tareas reales
        y aquí se imprimirá cada una con sus datos.
    """

    if task_list > 0:
        # Se imprime una línea de ejemplo por cada tarea que se haya añadido
        num_tareas = task_list

        while True:
            i = 0
            print("\nImpresión de tareas (simulación):\n")

            while i < num_tareas:
                print("Tarea ", i + 1, ".- Título tarea ", i + 1, " | Estado: completa/incompleta")
                # Se usaría la variable *completada* de la tarea número *i* para
                # poner el estado como "completa" o "incompleta"
                i += 1

            print("\nAquí se imprimen todas las tareas\n")

            opt = input("¿Quisieras:\n1. Leer alguna tarea completa\n2. Marcar alguna tarea como completada\n3. Eliminar una tarea\n4. Volver al menú principal\n> ")

            match(opt):
                case "1":
                    to_print = get_tarea_valida(task_list)
                    print("\nSe imprime la tarea número", to_print, "(ejemplo):\n")
                    print_task(task_list, to_print)

                    # Pendiente, imprimir la tarea número *to_print* de la lista de tareas
                case "2":
                    to_mark = get_tarea_valida(task_list)
                    print("\nSe marca la tarea ", to_mark, " como completada\n")
                    input("Presiona *Enter* para continuar\n>")

                    # Pendiente, poner la variable *completada* de la tarea número *to_mark* en True
                case "3":
                    to_del = get_tarea_valida(task_list)
                    print("\nSe elimina la tarea ", to_del, "\n")
                    task_list-=1

                    if(task_list == 0):
                        input("Ya no quedan mas tareas.\nAl menu principal\nPresiona *Enter* para continuar\n>")
                        print("")
                        break

                    # Pendiente, eliminar la tarea número *to_del*
                case "4":
                    print("\nVolviendo al menú principal\n")
                    break
                case _:
                    # Caso por defecto cuando el usuario no elige una opción válida
                    print("\nOpción inválida... ¡Intenta de nuevo!\n")
    else:
        print("\nNo hay tareas en la lista de tareas... ¡Añade una!\n")

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
                # Se llama a la función que añade una tarea nueva;
                # el contador de tareas aumenta en 1

                # Pendiente, añadir la tarea regresada a la lista de tareas
                task_list += add_task()
            case "3":
                # Se imprime un mensaje y se regresa a main para terminar el programa
                print("Saliendo del programa...")
                break
            case _:
                # Caso por defecto cuando el usuario no elige una opción válida
                print("Opción inválida... ¡Intenta de nuevo!\n")


def main():
    # Por el momento *task_list* es un contador de tareas (empieza en 0)
    # En un próximo avance será una lista con las tareas reales
    task_list = 0
    print("Se crea la lista de tareas vacía (contador en 0)\n")

    # Se pasa el contador a *menu*, ya que las funciones lo utilizarán
    menu(task_list)


if __name__ == "__main__":
    main()