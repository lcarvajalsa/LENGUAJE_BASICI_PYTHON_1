persona = {
    "firstName": "Luis Carlosl",
    "lastName": "Carvajal Sanchez",
    "age": 41,
    "id": 79922691,
    "state": True
}
# Muestra contenido Completo
print(persona)
# Muestra contenido por un Key particular
print(persona["age"])
# Muestra el valos de un Key en particular con metodo
print(persona.get("lastName"))
# cambiar datos
persona["firstName"] = "Jennifert Andrea"
print(persona.get("firstName"))
# incluir un Key
persona["Title"] = "Ingenieria Electronica"
print(persona["Title"])
# Acceder al valor
persona.update({"Nombre": "Pedro"})
print(persona)
# Borrar por propiedades
persona.pop("Title")
print(persona)
# Borra el ultimo
persona.popitem()
print(persona)
# Borrar apuntador especifico
del persona["lastName"]
print(persona)
# Mostrar Key
for x in persona:
    print(x)
# Mostrar valores
for y in persona:
    print(persona[y])
# recorrer conjunto de elementos
for x, y in persona.items():
    print(x, ":", y)
# anidados

i1 = {
    "firstName": "Luis Carlos",
    "lastName": "Carvajal Sanchez",
    "age": 41,
    "id": 79922691,
    "state": True
    }
i2 = {
    "firstName": "Luis Carlosl",
    "lastName": "Carvajal Sanchez",
    "age": 41,
    "id": 79922691,
    "state": True
    }
instructores = {
    "instructores1":i1,
    "instructores2":i2
}
print(instructores)

# Vaciar diccionario:
persona.clear()
print(persona)
# Borrar todo
del persona
