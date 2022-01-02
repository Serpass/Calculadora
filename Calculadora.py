print ("Calculadora, elija una opcion ingresando un numero:")
print ("1 - Suma")
print ("2 - Resta")
print ("3 - Multiplicacion")
print ("4 - Division")

opcion = int(input("Elija la opcion"))
def Suma(a,b):
    return(a+b)
def Resta(a,b):
    return(a-b)
def Multiplicacion(a,b):
    return(a*b)
def Division(a,b):
    return(a//b)
if(opcion == 1):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print (Suma(a, b))
elif(opcion == 2):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print (Resta(a, b))
    print ("opcion 2")
elif(opcion == 3):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    print (Multiplicacion(a, b))
    print ("opcion 3")
elif(opcion == 4):
    a = int(input("Ingrese el primer numero"))
    b = int(input("Ingrese el segundo numero"))
    if (b== 0 ):
        print("No se puede dividir entre cero")
    print (Division(a, b))
    print ("opcion 4")   
else:
    print("Elija la opcion entre 1 y 4")
