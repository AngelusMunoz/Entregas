import json

# -------------------------------
# CREAR DATOS INICIALES
# -------------------------------
libros = {
    "1": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel Garcia Marquez",
        "precio": 50000
    },
    "2": {
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "precio": 30000
    }
}

# -------------------------------
# GUARDAR JSON
# -------------------------------
with open("libros.json", "w", encoding="utf-8") as archivo:
    json.dump(libros, archivo, indent=4, ensure_ascii=False)

print("✅ Archivo de libros creado")


# -------------------------------
# LEER JSON
# -------------------------------
with open("libros.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("\n📖 Libros cargados:")
print(datos)


# -------------------------------
# ACCEDER A DATOS
# -------------------------------
print("\n📌 Accediendo a datos específicos:")
print("Titulo del libro 1:", datos["1"].get("titulo"))
print("Precio del libro 2:", datos["2"].get("precio"))


# -------------------------------
# ACTUALIZAR PRECIO
# -------------------------------
with open("libros.json", "r", encoding="utf-8") as archivo:
    datos_actuales = json.load(archivo)

datos_actuales["1"]["precio"] = 55000  # cambiamos precio

with open("libros.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)

print("\n💰 Precio actualizado correctamente")


# -------------------------------
# AGREGAR NUEVO LIBRO
# -------------------------------
with open("libros.json", "r", encoding="utf-8") as archivo:
    datos_actuales = json.load(archivo)

datos_actuales["3"] = {
    "titulo": "Harry Potter",
    "autor": "J.K Rowling",
    "precio": 45000
}

with open("libros.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)

print("📚 Nuevo libro agregado")


# -------------------------------
# ELIMINAR LIBRO
# -------------------------------
with open("libros.json", "r", encoding="utf-8") as archivo:
    datos_actuales = json.load(archivo)

del datos_actuales["2"]  # eliminamos el libro 2

with open("libros.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)

print("🗑️ Libro eliminado")


# -------------------------------
# MOSTRAR FINAL
# -------------------------------
with open("libros.json", "r", encoding="utf-8") as archivo:
    final = json.load(archivo)

print("\n📦 Estado final del JSON:")
print(final)