# Inicializamos una lista vacía para almacenar los diccionarios de productos
inventario = []

# Bucle principal para mantener el programa ejecutándose hasta que el usuario decida salir
while True:
    # Menú de opciones visual para el usuario
    print("""
1. agregar producto
2. mostrar inventario
3. calcular estadisticas
4. salir 
            """)
    
    # Captura la elección del usuario
    opcion = input("Que opcion desea realizar?: ")
    
    # Lógica para agregar un nuevo producto (Opción 1)
    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio: "))
        cantidad = int(input("Ingresa la cantidad: "))
        
        # Creamos un diccionario con los datos del producto
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
            }
        # Guardamos el diccionario dentro de nuestra lista 'inventario'
        inventario.append(producto)
        
    # Lógica para listar todos los productos guardados (Opción 2)
    elif opcion == "2":
        # Recorremos la lista y accedemos a las llaves de cada diccionario
        for elemento in inventario:
            print(f"Producto: {elemento['nombre']} | Precio: {elemento['precio']} | Cantidad {elemento['cantidad']}")

    # Lógica para realizar cálculos sobre el inventario (Opción 3)
    elif opcion == "3":
        total = 0 # Acumulador para el valor total
        for i in inventario:
            # Calculamos el valor por producto (precio x stock)
            valor = i["precio"] * i["cantidad"]
            print(f"El valor total del producto es: {i['nombre']} {valor} ")
            # Sumamos el valor del producto al total general
            total += valor  # Corregido: se usa += para sumar, no *=
            
        print("="*50)
        print("el valor total del inventario es:", total)
        print("="*50)

    # Lógica para cerrar el programa (Opción 4)
    elif opcion == "4":
        print("="*50)
        print("Gracias por utilizar mi programa")
        print("="*50)
        break # Rompe el bucle 'while' y termina la ejecución

    # hace el Manejo de errores por si el usuario ingresa algo que no está en el menú
    else:
        print("La opcion no es valida, por favor intenta nuevamente")
        continue # Regresa al inicio del bucle