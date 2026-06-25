cursos = []
#FUNCIONES
def agregar_cursos(cursos):
    print("<Agregar cursos>")
    while True:
            try:
                codigo = int(input("Ingresa que código se le asignará al curso: "))
                flag = False
                for curso in cursos:
                    if curso["codigo"] == codigo:
                        flag = True
                        break
                if flag == True:
                    print("El código ya está asociado en otro curso. Intente nuevamente.")
                else:
                    break
            except ValueError:
                print("Ingresa un valor númerico para el código del curso.")

    while True:
        nombre_curso = input("Ingesa el nombre del curso: ").strip()
        docente_curso = input("Ingresa el nombre del docente encargado: ").strip()
        if len(nombre_curso) == 0 or len(docente_curso) == 0:
            print("El nombre del docente o nombre del curso, no pueden estar vacíos.")
        else:
            nombre_curso = nombre_curso.lower().title()
            docente_curso = docente_curso.lower().title()
            break
    
    while True:
        try:
            cant_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
            if cant_estudiantes <= 0:
                print("La cantidad de estudiantes no pueder igual o menor a 0.")
            else:
                break
        except ValueError:
            print("Ingrese una cantidad válida de estudiantes. Intente nuevamente.")

    curso_agregado = {"codigo": codigo,
                      "nombre": nombre_curso,
                      "docente": docente_curso,
                      "cantidad": cant_estudiantes}
    
    cursos.append(curso_agregado)
    print("Curso agregado exitosamente.")

def listar_cursos(cursos):
    print("<Lista de crusos agregados>")

    if len(cursos) == 0:
        print("No hay cursos agregados.")
    else:
        for curso in cursos:
            print(f"Código del curso: {curso["codigo"]}")
            print(f"Nombre del curso: {curso["nombre"]}")
            print(f"Docente encargado: {curso["docente"]}")
            print(f"Cantidad de alumnos: {curso["cantidad"]}")
            print("=======================================")

def buscar_curso(cursos):
    print("<Buscar cursos>")
    try:
        cod = int(input("Ingresa el código del curso a buscar: "))
    except ValueError:
        print("Ingrese un código númerico.")
    for curso in cursos:
        if cod == curso["codigo"]:
            print("¡Curso encontrado!")
            print(f"Código del curso: {curso["codigo"]}")
            print(f"Nombre del curso: {curso["nombre"]}")
            print(f"Docente encargado: {curso["docente"]}")
            print(f"Cantidad de alumnos: {curso["cantidad"]}")
            print("=======================================")
            return
        else:
            print("No se encontró ningún curso con ese código asociado.")
            return

def eliminar_curso(cursos):
    print("<Eliminar curso>")
    try:
        cod = int(input("Ingresa el código del curso a eliminar: "))
    except ValueError:
        print("Ingresa un código númerico.")

    for curso in cursos:
        if cod == curso["codigo"]:
            print("¡Curso encontrado!")
            print(f"Código del curso: {curso["codigo"]}")
            print(f"Nombre del curso: {curso["nombre"]}")
            print(f"Docente encargado: {curso["docente"]}")
            print(f"Cantidad de alumnos: {curso["cantidad"]}")

            op = input("¿Eliminar el curso?(s/n): ").lower()
            if op == "s":
                cursos.remove(curso)
                print("Curso eliminado exitosamente.")
                return
            elif op == "n":
                print("Operación cancelada.")
                return
            else:
                print("Ingresa una opción válida, 's' para sí o 'n' para no.")
                return
        else:
            print("No se encontró ningún curso asociado a ese código.")
            return
        
#MENÚ CRUD
print("=====SISTEMA CRUD PARA ADMINISTRAR CURSOS=====")
while True:
    print("1. Agregar curso.\n" \
    "2. Listar curso.\n" \
    "3. Buscar curso.\n" \
    "4. Eliminar curso\n" \
    "5. Salir.")

    op = input("Ingrese la opción a realizar: ")

    if op == "1":
        agregar_cursos(cursos)
    elif op == "2":
        listar_cursos(cursos)
    elif op == "3":
        buscar_curso(cursos)
    elif op == "4":
        eliminar_curso(cursos)
    elif op == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Ingrese una opción válida. Intente nuevamente.")

print("Gracias por usar nuestros servicios.")