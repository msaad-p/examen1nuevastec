import uuid

def pedirDatosHelado():
    nombre = input("Ingresa el nombre del helado que quieres pedir: ")
    descripcion = input("Ingresa la descripción de tu helado: ")
    while True:
        try:
            cantidad = int(input("¿Cuántos helados de este tipo vas a ordenar?: "))
            break
        except ValueError:
            print("Ingrese un número entero de helados")
    while True:
        try:
            precioUnitario = int(input("Ingresa el precio individual del helado en COP: "))
            break
        except ValueError:
            print("Ingrese un precio válido, en números enteros")
    
    return nombre, descripcion, cantidad, precioUnitario

def crearHelado(helado, nombre, descripcion, cantidad, precioUnitario):
    helado["ID"]=str(uuid.uuid4().hex[:8]) #Usado con ChatGPT para conocer funcionamiento de la libreria, tomando los primeros 8 dígitos del ID para que no sea tan largo
    helado["Nombre"]=nombre
    helado["Descripción"]=descripcion
    helado["Cantidad"]=cantidad
    helado["Precio Unitario"]=precioUnitario
    return helado

def agregarHelado(helado, helados):
    helados.append(helado)
    return helados

def verHelado(helados):
    n=0
    for helado in helados:
        n=n+1
        print("")
        print("Helado",n)
        for clave, valor in helado.items():
            print(f"{clave}: {valor}")

def modificarHelado(helados, id):
    for helado in helados:
        if helado["ID"] == id:
            print("Ingresa los nuevos datos:")
            nombre, descripcion, cantidad, precioUnitario = pedirDatosHelado()
            helado["Nombre"] = nombre
            helado["Descripción"] = descripcion
            helado["Cantidad"] = cantidad
            helado["Precio Unitario"] = precioUnitario
            print("Se modificó el helado")
            return
    print("No hay ningún helado con ese ID")

def eliminarHelado(helados, id):
    for helado in helados:
        if helado["ID"] == id:
            helados.remove(helado)
            print("Se eliminó el helado")
            return
    print("No hay ningún helado con ese ID")

