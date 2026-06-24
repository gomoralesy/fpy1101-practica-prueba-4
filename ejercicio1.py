estudiantes = []

def registrar_estudiantes(estudiantes):
    for i in range(3):
        print(f"INGRESO DEL ESTUDIANTE - {i+1}")
        while True:
            rut = input("Ingrese el rut del estudiante: ").strip()
            if (len(rut) == 0):
                print("El rut no puede estar vacío.")
            else:
                break
 
        while True:
            nom_estudiante = input("Ingrese el nombre del estudiante: ").strip()
            if (len(nom_estudiante) == 0):
                print("El nombre del estudiante no puede estar vacío.")
            else:
                nom_estudiante = nom_estudiante.lower().title()
                break

        while True:
            try:
                edad = int(input("Ingresa la edad del estudiante: "))
                if edad < 18:
                    print("La edad debe ser un número entero mayor o igual a 18.")
                else:
                    break
            except ValueError:
                print("Ingrese un valor válido. Intente nuevamente.")
        
        while True:
            carrera = input("Ingresa la carrera del estudiante: ").strip()
            if (len(carrera) == 0):
                print("La carrera no puede estar vacía.")
            else:
                carrera = carrera.lower().title()
                break

        lista_estudiante = {"rut": rut,
                            "nombre": nom_estudiante,
                            "edad": edad,
                            "carrera": carrera}
        
        estudiantes.append(lista_estudiante)
        print("Estudiante registrado exitosamente.")

def mostrar_estudiantes(estudiantes):
    print("[LISTA DE ESTUDIANTES]")
    for estudiante in estudiantes:
        print(f"Rut del estudiante: {estudiante["rut"]}")
        print(f"Nombre del estudiante: {estudiante["nombre"]}")
        print(f"Edad del estudiante: {estudiante["edad"]}")
        print(f"Carrera del estudiante: {estudiante["carrera"]}")
        print("=========================================")

registrar_estudiantes(estudiantes)
mostrar_estudiantes(estudiantes)