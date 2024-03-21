# Diccionario con Información Personal
informacion_personal = {"Nombre": "Dahere Daladier Llerena","Edad": 24,"Ciudad": "Cayambe",}
# Accedemos al valor asociado a la clave "ciudad"
ciudad_actual = informacion_personal["Ciudad"]
# Modificamos el valor de la clave "ciudad" por una nueva ciudad
informacion_personal["Ciudad"] = "Ibarra"
# Agregamos una nueva clave "profesion" con un valor ficticio
informacion_personal["Profesion"] = "Militar"
# Verificamos si la clave "telefono" existe
if "Telefono" in informacion_personal:
    print(f"Teléfono: {informacion_personal['Telefono']}")
else:
    print("La clave 'Telefono' no existe en el diccionario")
# Eliminamos la clave "edad" del diccionario
del informacion_personal["Edad"]
# Imprimimos el diccionario con todas las modificaciones realizadas
print(informacion_personal)
