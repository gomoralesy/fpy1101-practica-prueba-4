print("=====SISTEMA DE NOTAS POR ESTUDIANTE=====")
estudiantes = []

def registrar_estudiantes():
        nom_estudiante = input("Ingresa el nombre del estudiante(Escribe fin para terminar de registrar.): ").lower().title()
        return nom_estudiante

def validar_nota(entrada):
        while True:
                try:
                    nota = float(input(entrada))
                    return nota
                except ValueError:
                    print("Debe ingresar una nota válida entre 1.0 y 7.0")

def calcular_promedio(n1,n2,n3):
        promedio = (n1+n2+n3) / 3
        return promedio

def determinar_estado(promedio):
        if promedio >= 4.0:
                estado = "Aprobado."
                return estado
        elif promedio < 4.0:
                estado = "Reprobado."
                return estado
        
def mostrar_estudiantes(estudiantes):
        for estudiante in estudiantes:
                print(f"Nombre del estudiante: {estudiante["nombre"]}")
                print(f"Promedio: {estudiante["promedio"]}")
                print(f"Estado: {estudiante["estado"]}")
                print("===================================")

estudiante = registrar_estudiantes()
while estudiante != "Fin":
        nota1 = validar_nota("Ingrese la nota 1: ")
        nota2 = validar_nota("Ingrese la nota 2: ")
        nota3 = validar_nota("Ingrese la nota 3: ")
        promedio = calcular_promedio(nota1,nota2,nota3)
        estado = determinar_estado(promedio)
        estudiante_agregado = {"nombre": estudiante,
                               "promedio": promedio,
                               "estado": estado}
        estudiantes.append(estudiante_agregado)
        estudiante = registrar_estudiantes()

mostrar_estudiantes(estudiantes)

        