# Definimos las variables iniciales
# nombre empieza vacío, precio y cantidad empiezan en -1
# para obligar al usuario a ingresar valores válidos
nombre = ""
precio = -1
cantidad = -1


# Este ciclo se repite hasta que el usuario ingrese un nombre que solo tenga letras (sin números ni símbolos)
while not nombre.isalpha():
    nombre = input("Ingrese el nombre del producto: ")
    
    # Si el nombre tiene algo que no sea letras se muestra un mensaje de error
    if not nombre.isalpha():
        print("Ingresa solamente el nombre, no números ni decimales ni negativos")


# Este ciclo se repite hasta que el usuario ingrese
# un precio válido mayor o igual a 0
while precio < 0:
    try:
        # Se pide el precio y se convierte a número decimal (float)
        precio = float(input("Ingrese el precio: "))
        
        # Si el precio es negativo se muestra un error
        if precio < 0:
            print("El precio no puede ser negativo")
    
    # Si el usuario escribe algo que no sea número
    except:
        print("Ingresa solo números")


# Este ciclo se repite hasta que el usuario ingreseuna cantidad válida mayor o igual a 0
while cantidad < 0:
    try:
        
        cantidad = int(input("Ingresa la cantidad: "))
        
        # Si la cantidad es negativa se muestra un error
        if cantidad < 0:
            print("La cantidad no puede ser negativa")
    
    # Si el usuario escribe algo que no sea un número entero
    except:
        print("Ingresa solo números enteros")


# Aquí se calcula el costo total del producto
costo_total = precio * cantidad


# Se muestran los datos del producto registrado y el costo total
print("\nProducto registrado:")
print("Nombre:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print(f"Costo total calculado ${costo_total}")