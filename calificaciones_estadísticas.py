'''
El programa que vas a desarrollar en este entrenamiento debe:
Determinar el estado de aprobación:
    Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
Calcular el promedio:
    Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    Calcular y mostrar el promedio de las calificaciones en la lista
Contar calificaciones mayores:
    Preguntar al usuario por un valor específico
    Contar cuántas calificaciones en la lista son mayores que este valor
Verificar y contar calificaciones específicas:
    Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    Calcular y mostrar el promedio de las calificaciones en la lista


'''



listaFinal = []

def qualifi():

    name= input("Por favor ingresar el nombre del estudiante ")
    dictionary["name"]= name
    while True:
        note = input("por favor ingresar las notas del estudiante separados por , ").split(",")
        try:
            for x in note:
                float(x)
                print(f"Funciona{type(x)}")
                qualifications.append(float(x))


            dictionary["qualifications"]=qualifications
            break
        except:
            print(f"Error no valido {x}")

while True:
    qualifications = []
    dictionary= {}
    qualifi()
    print(qualifications)
    resultado=0
    for i in qualifications:
        resultado += i

    resultado = round(resultado/len(qualifications),2)
    dictionary["prom"]=resultado
    listaFinal.append(dictionary)
    print(listaFinal)
    print("\n\n\n")





#qualifications = input("por favor ingresar las notas del estudiante separados por , ").split(",")
'''

print(qualifications)
nuevo = [float(x) for x in qualifications ]
print(f"quialificatiosn = {len(qualifications)}¸\n")
print(f"len students_nuesvos= {len(nuevo)} len quialificatiosn = {(nuevo)} --- {type(nuevo[0])}")

'''

#45.24, 49.36, 75.24