
import os
studiens_dictionary = {}
student_id = 1

#funcion para calcular cuantes veces aparece una nota
def equal_number():
    while True:
        if not studiens_dictionary:
            print("No hay estudiantes registrados ")
            return

        try: 
            search_number= float(input("Por favor ingresar un numero especifico que quieras buscar: "))
            if (0 <= search_number <= 100  ):
                number_total = 0
                for studen_id, data in studiens_dictionary.items():
                    quilifecat = data.get("qualifications", [])
                    name = data.get("name", "none")

                    count = 0
                    a=0
                    while a < len(quilifecat):
                        if quilifecat[a]== search_number:
                            count +=1
                            a+=1
                            continue
                        a+=1
                    if count > 0:
                        #print("entro")
                        print(f"El estudiante { name} tiene {count} calificaciones de valor {search_number}")
                    else:
                        print(f"El estudiante {name} no tiene calificaciones con {search_number}")
                        break

            else:
                print("valor no valido")
                continue
        except:
            print("Ingresa un numero valido ")
            return
        
        repit= input("¿Deseas hacer otra comparación? (si/no): ")
        if repit != "si":
            break
        
# funcion para calcualar notas mayores a una especifica, si no tiene notas de estudiantes pregunta si quiere agregar
def numberGreater():
    while True:
        if studiens_dictionary:
            try:
                value_greater = float(input("Ingrese el valor para comparar: "))

                total_mayores = 0  
                for  student_id, data in studiens_dictionary.items():
                    lista = data.get('qualifications', [])
                    count = 0
                    for nota in lista:
                        if nota > value_greater:
                            count += 1

                    print(f"Estudiante {data['name']} tiene {count} notas mayores a {value_greater}")
                    total_mayores += count
                    

                print(f"\nEn total hay {total_mayores} notas mayores a {value_greater} entre todos los estudiantes.")

                repit= input("¿Deseas hacer otra comparación? (si/no): ")
                if repit != "si":
                    break

            except ValueError:
                print("Error: no ingresaste un número valido.")
                break
        else:
            data = input("No tienes notas de ningún estudiante. Quieres ingresar alguno? (si para continuar): ")
            if data.lower() == "si":
                qualifi()
                continue
            break


#funcion para ingresar estudiantes pide nombre del estudiante y las notas puede meter 1 o mas 
def qualifi():
    global student_id 
    name = input("Por favor ingresar el nombre del estudiante ")
    studiens_dictionary[student_id] = {'name': name}
    
    while True:
        note = input("Por favor ingresar notas separadas por coma entre 0 y 100: ").split(",")
        try:
            qualifications = [float(x) for x in note]
            if all(0 <= x <= 100 for x in qualifications):
                average = round(sum(qualifications) / len(qualifications), 2)
                studiens_dictionary[student_id]['qualifications'] = qualifications
                studiens_dictionary[student_id]['average'] = average
                studiens_dictionary[student_id]['status'] = (
                    "Aprobado" if average >= 60 else "Reprobado"
                )
                #print(f"Estudiante agregado: {studiens_dictionary[student_id]}")
                print(f"El promedio de {name} es de {average} y {studiens_dictionary[student_id]['status']} la materia")
                student_id += 1  
                break
            else:
                print("Todas las notas deben estar entre 0 y 100.")
        except ValueError:
            print("Por favor ingrese solo números válidos.")

# funcion para mostar los estudiantes agregados 
def seeStudent():
    if not studiens_dictionary:
        print("No hay estudiantes registrados.")
        return
    
    for sid, data in studiens_dictionary.items():
        print(f"ID: {sid} | Nombre: {data['name']} | Promedio: {data['average']} | Estado: {data['status']}")

menu='''
    1. para ingresar calificaciones de estudiante 
    2. Verificar promedio mayor a un numero
    3. Verificar un numero especifico  
    4. Ver lista de estudiantes 

    '''

while True:
# os.system("clear")
    
    case = (input(menu))
    #try:
    if case == '1':
        qualifi()
    elif case == '2':
        numberGreater()
    elif case == '3':
        equal_number()
    elif case =='4':
        seeStudent()
    print("\n")