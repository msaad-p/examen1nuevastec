from funciones import pedirFruta, mostrarFrutas, ordenarFrutasPorPrecio

frutas = []
print("¡Bienvenide al organizador de frutas para tu salpicón!")

for i in range(10):
    print("")
    print(f"Fruta {i+1}/10:")
    nombre, precio = pedirFruta()
    fruta = {"Nombre": nombre, "Precio": precio}
    frutas.append(fruta)

ordenarFrutasPorPrecio(frutas)
mostrarFrutas(frutas)
