
# escribe un programa en py. que impirma los numeors del 1 al 100 pero siguiendo las siguientes reglas

'''
 - por cada numero divisible por 3, imprime "Fizz"
 - por cada numero d por 5 impirme "Buzz!
 - para los numero d por ambos 3 y 5 imprime "FizzBuzz"
 - si el numero no es fivisible ni por 3 ni por 5 imprime el numero    
 

for i in range(1, 101):
    
    if(i%3 ==0  and i%5 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)
        
'''
'''

tex= ".upper() para mayusculas"
x= (tex.upper()) #.UPPER() PARA MAYUSCULAS
print(x)


a = ".LOWER() PARA PONER EN MINUSCULAS  "
b = a.lower()   #.lower() para poner en minusculas 
print(b)


#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print(5>3)

'''


#pide al ususario su edad y muestra
'''
 - eres un niño --> si tiene 12 años, 
 - eres adolecente si teiene entre 12 y 17
 - eres un adulto si tiene entre 18 y 59
 - eres un adulto mayor si tiene 60 o mas


'''


while True:
    
    try:
        edad = int(input("¿Cuántos años tienes? "))
        if edad < 0:
            print("La edad no puede ser negativa.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")
if edad <= 12:      
    print("Eres un niño.")
elif edad <= 17:                            
    print("Eres un adolescente.")
elif edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")





