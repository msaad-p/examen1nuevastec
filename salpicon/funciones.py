def pedirFruta():
    nombre = input("Ingresa el nombre de la fruta: ")
    while True:
        try:
            precio = int(input(f"Ingresa el precio de {nombre} en COP: "))
            break
        except ValueError:
            print("Ingresa un número válido para el precio")
    return nombre, precio


def mostrarFrutas(frutas):
    n = 0
    print("")
    print("--- Frutas ordenadas de mayor a menor precio ---")
    print("")
    for fruta in frutas:
        n += 1
        nombre = fruta["Nombre"]
        precio = fruta["Precio"]
        print(f"{n}. {nombre}: {precio}")


def ordenarFrutasPorPrecio(frutas):
    frutas.sort(key=lambda fruta: fruta["Precio"], reverse=True) #Uso de ChatGPT para uso correcto de la función sort, lambda es la funcion anónima que toma el diccionario fruta y solo toma el parámetro precio.
    return frutas
