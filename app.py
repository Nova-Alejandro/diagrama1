import archivos  

inventario = []

def Agregar_nuevo_producto():
    try:
        cantidad_productos = int(input("¿Cuántos productos deseas agregar?: "))
        # El ID se basa en el último elemento si existe, para evitar duplicados
        id_actual = inventario[-1]['id_producto'] + 1 if inventario else 1

        for idx in range(cantidad_productos):
            nombre = str(input(f"Ingresa el nombre del Producto {idx+1}: "))
            precio = float(input(f"Ingresa el precio del producto {idx+1}: "))
            cantidad = int(input(f"Ingresa la cantidad del producto {idx+1}: "))
            
            nuevo_producto = {
                "id_producto": id_actual,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            
            inventario.append(nuevo_producto)
            print(f"Producto '{nombre}' agregado con éxito.")
            id_actual += 1
    except ValueError:
        print("Error: Ingresa valores numéricos válidos para precio y cantidad.")

def Mostrar_inventario():
    if not inventario:
        print("\n[!] No hay nada en el inventario.")
    else:
        print("\n--- INVENTARIO ACTUAL ---")
        for producto in inventario:          
            print(f"ID: {producto['id_producto']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Stock: {producto['cantidad']}")

def Buscar_el_producto():
    try:
        busqueda = int(input("Ingresa el ID del producto que deseas buscar: "))
        encontrado = False 
        for producto in inventario:
            if busqueda == producto['id_producto']: 
                print(f"\nResultado: ID: {producto['id_producto']} | Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró el producto con ese ID.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def Actualizar_Producto():
    try:
        actualizar = int(input("ID del producto que desea actualizar: "))
        encontrado = False
        for producto in inventario:
            if actualizar == producto['id_producto']:
                encontrado = True
                tipo = input("¿Qué dato deseas actualizar? (nombre/precio/cantidad): ").lower()
                if tipo == "nombre":
                    producto['nombre'] = input("Nuevo nombre: ")
                elif tipo == "precio":
                    producto['precio'] = float(input("Nuevo precio: "))
                elif tipo == "cantidad":
                    producto['cantidad'] = int(input("Nueva cantidad: "))
                else:
                    print("Dato no válido.")
                    return
                print("Producto actualizado correctamente.")
                break
        if not encontrado:
            print("No se encontró el producto.")
    except ValueError:
        print("Error: Entrada de datos no válida.")

def Eliminar_producto():
    try:
        id_eliminar = int(input("ID del producto que desea eliminar: "))
        for i, producto in enumerate(inventario):
            if producto['id_producto'] == id_eliminar:
                eliminado = inventario.pop(i)
                print(f"El producto '{eliminado['nombre']}' ha sido eliminado.")
                return
        print("No se encontró el producto a eliminar.")
    except ValueError:
        print("Error: El ID debe ser un número.")

def Calcular_estadistica():
    if not inventario:
        print("El inventario está vacío.")
        return

    unidades_totales = 0
    valor_total = 0
    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += (producto["precio"] * producto["cantidad"])

        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("\n----- ESTADÍSTICAS -----")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con más stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")

def Cargar_Desde_Archivo():
    ruta = input("Nombre del archivo CSV (ej: datos.csv): ")
    datos_nuevos, errores = archivos.cargar_csv(ruta)

    if datos_nuevos is None:
        return

    opcion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    
    if opcion == 'S':
        inventario.clear()
        for i, p in enumerate(datos_nuevos, 1):
            p['id_producto'] = i
            inventario.append(p)
        print(f"\nResumen: Inventario sobrescrito con {len(datos_nuevos)} productos. ({errores} errores omitidos).")
    else:
        # Fusión por nombre
        nuevos_cont = 0
        actualizados_cont = 0
        for p_nuevo in datos_nuevos:
            encontrado = False
            for p_actual in inventario:
                if p_actual['nombre'].lower() == p_nuevo['nombre'].lower():
                    p_actual['cantidad'] += p_nuevo['cantidad']
                    p_actual['precio'] = p_nuevo['precio'] # Actualiza al precio más reciente
                    actualizados_cont += 1
                    encontrado = True
                    break
            
            if not encontrado:
                # Asignar nuevo ID
                nuevo_id = inventario[-1]['id_producto'] + 1 if inventario else 1
                p_nuevo['id_producto'] = nuevo_id
                inventario.append(p_nuevo)
                nuevos_cont += 1
        
        print(f"\nResumen: {nuevos_cont} nuevos, {actualizados_cont} actualizados. ({errores} errores omitidos).")

# Menú Principal
while True:
    print("""
================================
    SISTEMA DE INVENTARIO
================================
    1. Agregar nuevos Productos
    2. Mostrar el Inventario
    3. Buscar un Producto
    4. Actualizar Producto
    5. Eliminar Producto
    6. Calcular Estadísticas
    7. Cargar desde CSV (Persistencia)
    8. Salir del programa
=================================""")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        Agregar_nuevo_producto()
    elif opcion == "2":
        Mostrar_inventario()
    elif opcion == "3":
        Buscar_el_producto()              
    elif opcion == "4":
        Actualizar_Producto()
    elif opcion == "5":
        Eliminar_producto()
    elif opcion == "6":
        Calcular_estadistica()
    elif opcion == "7":
        Cargar_Desde_Archivo()
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
