#9. Spa: servicio disponible
#En un spa hay estos servicios:
#• masaje
#• facial
#• manicure
#Pide al usuario qué servicio desea y muestra un mensaje confirmando
#si existe o no.
#Practica: condicionales con texto.


print("===========================================")
print("              SPA  ANGELUS                 ")
print("===========================================")

print("Bienvenido al Spa Angelus")
print("Nuestros servicios son:")
print("- Masaje")
print("- Facial")
print("- Manicure")

servicio = input("Ingrese el servicio que desea: ")

if servicio == "masaje":
    print("Servicio disponible: masaje")

elif servicio == "facial":
    print("Servicio disponible: facial")

elif servicio == "manicure":
    print("Servicio disponible: manicure")

else:
    print("Lo lamentamos, ese servicio no existe")