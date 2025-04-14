from funciones import crearHelado, agregarHelado, pedirDatosHelado, verHelado, modificarHelado, eliminarHelado
helados=[]

print("¡Bienvenide! A continuación vamos a crear tu lista de helados.")

opcion=0
while opcion!=5:
    helado={}
    print("""Escoge una opción del menú:
          --MENÚ--
      1. Crear un helado
      2. Ver la lista de helados
      3. Modificar un helado
      4. Eliminar un helado
      5. Salir""")
    
    while True:
        try:
            opcion = int(input("Ingresa tu opción: "))
            break
        except ValueError:
            print("Ingresa un número del 1 al 5.")

    if opcion==1:
        print("Has ingresado a CREAR UN HELADO")
        nombre, descripcion, cantidad, precioUnitario=pedirDatosHelado()
        crearHelado(helado, nombre, descripcion, cantidad, precioUnitario)
        agregarHelado(helado, helados)
        print("")

    elif opcion==2:
        print("Has ingresado a VER LA LISTA DE HELADOS")
        verHelado(helados)
        print("")

    elif opcion==3:
        print("Has ingresado a MODIFICAR UN HELADO")
        idH=input("Ingresa el ID del helado que quieres modificar: ")
        modificarHelado(helados, idH)
        print("")

    elif opcion==4:
        print("Has ingresado a ELIMINAR UN HELADO")
        idH=input("Ingresa el ID del helado que quieres eliminar: ")
        eliminarHelado(helados, idH)
        print("")

    elif opcion==5:
        print("Has salido del programa, ¡gracias!")
    else:
        print("Opción inválida, intenta de nuevo con una opción válida")
