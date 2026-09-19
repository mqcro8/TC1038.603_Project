# Avance 2 Proyecto

**Lista de tareas (TODO) — Esqueleto funcional en Python**

**Miguel Ceballos Aguilar - A01716791**
**Tecnológico de Monterrey, Campus Querétaro**  
**TC1038 – Fundamentos de Programación**  
**Proyecto Integrador – Avance 2**  
**Profesor: Dr. Leonardo Ledesma Domínguez**

---

## Sobre este avance

En este segundo avance del Proyecto Integrador se transforma la propuesta
desarrollada en el Avance 1 en una primera versión programada en Python.

El objetivo no es que el proyecto esté terminado, sino construir un
**esqueleto funcional** del programa que muestre su estructura general y
aplique correctamente los conceptos de programación estudiados durante las
primeras cinco semanas del curso (variables, condicionales, ciclos,
funciones y selección de casos con `match`).

## ¿De qué trata el proyecto?

Es una aplicación de **lista de tareas (TODO)** que permite llevar un
registro de los pendientes personales y escolares.

## Define el problema

### ¿En qué consiste el problema?

Soy muy desorganizado, por lo que quisiera desarrollar una herramienta que
me ayudara a mantenerme al corriente con la escuela, proyectos personales,
tareas, etc.

### ¿Por qué resulta interesante o útil resolverlo?

Ya que me ayudaría a asegurarme de que no hay ninguna fecha límite de
entrega de alguna tarea, o de registro a una competencia. Además me permite
no perderme y no olvidarme de mis pendientes.

### ¿Qué deberá realizar el programa?

Guardar las tareas o pendientes por hacer, y la fecha para la cual debo
haberlas completado o entregado.

## Estado actual del programa

Es un esqueleto funcional que muestra la estructura general de la aplicación:

- **Menú principal** con tres opciones: ver tareas, añadir tarea y salir.
- **Añadir tarea**: solicita el nombre, la fecha límite y la descripción
  (por el momento es una simulación y solo aumenta el contador de tareas).
- **Ver tareas**: simula la impresión de las tareas (una línea por cada tarea
  añadida) y muestra un submenú con las acciones de leer una tarea completa,
  marcarla como completada, eliminarla o volver al menú principal. Si se pide
  un número de tarea que no existe, se avisa cuántas hay y se vuelve a pedir.

> **Nota:** como aún no se estudian las listas en el curso, el programa usa un
> contador para llevar el total de tareas.

### Pendiente para los próximos avances

- Guardar los datos reales de cada tarea (nombre, fecha límite, descripción).
- Marcar tareas como completadas.
- Eliminar tareas.
- Imprimir por completo los datos de cada tarea.

## Cómo ejecutarlo

Se requiere **Python 3.10 o superior** (el código usa la sentencia `match`).

Desde la terminal, dentro de la carpeta del proyecto:

```
python A01716791_ap2.py
```

## Estructura del código

| Función | Descripción |
|---------|-------------|
| `main()` | Crea el contador de tareas (empieza en 0) e inicia el menú. |
| `menu()` | Muestra el menú principal y dirige al usuario a cada opción. |
| `add_task()` | Pide los datos de la nueva tarea y regresa 1 para aumentar el contador. |
| `print_tasks()` | Simula la impresión de todas las tareas y muestra el submenú de acciones. |
| `print_task()` | Ejemplo de cómo se imprimiría una tarea completa. |
| `get_tarea_valida()` | Pide un número de tarea y verifica que exista (entre 1 y el total de tareas). |