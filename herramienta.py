import requests as r
import datetime as d
import phonenumbers
from phonenumbers import timezone, carrier, geocoder

fecha = d.date.today()
print(f"iniciaste secion el {fecha}")
print("herramienta hecha por Yuki")
print()

clave = ""
while True:
    clave = input("escribe contraseña: ")
    if clave == "kaguya12":
        print("contraseña correcta puedes pasar")
        break
    else:
        print("contraseña incorrecta vuelve a intentar")
print()        
op = input("elige a para ver direccion ip y b para usar calculadora y c para ver informacion de numero de celular: ").lower()
if op == "a":         
   ip = input("ingresa direccion ip: ")
   url = f"http://ip-api.com/json/{ip}"
   respuesta = r.get(url)
   datos = respuesta.json()
   print()
   print("información obtenida:")
   print("pais:", datos["country"])
   print("ciudad:", datos["city"])
   print("region:", datos["regionName"])
   print("longitud:", datos["lon"])
   print("latitud:", datos["lat"])
   print("provedor:", datos["isp"])
   print("hora:", datos["timezone"])
   
elif op == "b":
    num1 = float(input("escribe primer numero: "))
    num2 = float(input("escribe 2 digito: "))
    oprc = input("A para sumar, B para restar C para multiplicar y D para divir: ").lower()
    if oprc == "a":
        print(num1 + num2)
    elif oprc == "b":
        print(num1 - num2)
    elif oprc == "c":
        print(num1 * num2)
    elif oprc == "d":
        print(num1 / num2)
    else:
        print("no es una opcion")

elif op == "c":
    
  numero = input("escribe numero: ")
  info = phonenumbers.parse(numero)
  hora = timezone.time_zones_for_number(info)
  ubicacion = carrier.name_for_number(info, 'en')
  Region = geocoder.description_for_number(info, 'en')
  codigo_pais = info.country_code
  tipo_numero = phonenumbers.number_type(info)
  
  print(f"la hora del numero es: {hora}")
  print(f"la ubicacion es: {ubicacion}")
  print(f"la Region del numero es: {Region}")
  print(f"el codigo de pais es: {codigo_pais}")
  print(f"el tipo de numero es {tipo_numero}")
  

  
