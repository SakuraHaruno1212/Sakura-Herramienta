def sumar(a, b):
    return a + b
    
    
def comprobar():
    edad = int(input("escribe tu edad: "))
    if edad >= 18:
        print("es mayor de edad")
    elif edad < 18:
        print("eres menor de edad")
        

def preguntar():
    pgt = input("naim es fuerte o debil?: ")
    if pgt == "debil" or pgt == "debíl":
        print("si es debil xd")
    elif pgt == "fuerte":
        print("no es debil y la burla")
    else:
        print("esa no es una opción")
        
