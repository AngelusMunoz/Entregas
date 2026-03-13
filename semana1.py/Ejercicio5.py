#5. Tienda de mascotas: alimento por tipo de animal
#Pide el tipo de mascota:
#• perro
#• gato
#• conejo
#Luego muestra una recomendación de alimento según el animal.
#Practica: comparaciones con texto.

print("===========================================")
print("                 PET CITY                  ")
print("===========================================")

print("Bienvenido a Pet City.")
print("Ofrecemos todo tipo de productos para los caninos, felinos y conejos.")
mascota = str(input("Porfavor, ingrese la especie de su mascota para tener una recomendacion para su dieta: ")).lower()


if mascota == "perro" or mascota == "canino":
    print("Para su amigo perruno, Pet City le recomienda la linea de alimentos Pedigree.")

elif mascota == "gato" or mascota == "felino":
    print("Para su amigo gatuno, Pet City le recomienda la linea de alimentos Whiskas.")

elif mascota == "conejo" or mascota == "lagomorpha":
    print("Para su amigo de orejas largas, Pet City le recomienda la linea de alimentos Oxbow.")

else:
    print("Lo sentimos, aun no tenemos productos disponibles para su mascota.")