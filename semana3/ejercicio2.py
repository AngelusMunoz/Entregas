import json

# -------------------------------
# CREAR CLIENTES
# -------------------------------
clientes = {
    "1": {
        "nombre": "Carlos",
        "edad": 30,
        "compras": [20000, 15000]
    },
    "2": {
        "nombre": "Maria",
        "edad": 25,
        "compras": [5000]
    }
}

# -------------------------------
# GUARDAR JSON
# -------------------------------
with open("clientes.json", "w", encoding="utf-8") as archivo:
    json.dump(clientes, archivo, indent=4, ensure_ascii=False)

print("✅ Archivo de clientes creado")


# -------------------------------
# LEER JSON
# -------------------------------
with open("clientes.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("\n👥 Clientes cargados:")
print(datos)


# -------------------------------
# CALCULAR TOTAL DE COMPRAS
# -------------------------------
print("\n💸 Total gastado por cliente:")
for id_cliente, info in datos.items():
    total = sum(info["compras"])
    print(f"{info['nombre']} ha gastado: ${total}")


# -------------------------------
# AGREGAR NUEVA COMPRA
# -------------------------------
with open("clientes.json", "r", encoding="utf-8") as archivo:
    datos_actuales = json.load(archivo)

datos_actuales["1"]["compras"].append(30000)

with open("clientes.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)

print("\n🛒 Compra agregada correctamente")


# -------------------------------
# AGREGAR NUEVO CLIENTE
# -------------------------------
with open("clientes.json", "r", encoding="utf-8") as archivo:
    datos_actuales = json.load(archivo)

datos_actuales["3"] = {
    "nombre": "Laura",
    "edad": 28,
    "compras": []
}

with open("clientes.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)

print("👤 Nuevo cliente agregado")


# -------------------------------
# MOSTRAR FINAL
# -------------------------------
with open("clientes.json", "r", encoding="utf-8") as archivo:
    final = json.load(archivo)

print("\n📦 Estado final:")
print(final)