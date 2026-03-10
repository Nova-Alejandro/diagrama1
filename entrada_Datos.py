nombre = ""
precio = -1
cantidad = -1

while  not nombre.isalpha():
            nombre = input("ingrese un nombre del producto: ")
            if not nombre.isalpha():
                    print("ingresa solamente el nombre , no numeros ni decimales ni negativos")
        
while precio < 0:
    try:
        precio = float(input("Ingrese el precio: "))
        if precio < 0:
            print("El precio no puede ser negativo")
    except:
        print("Ingresa solo números")
    
while cantidad < 0:
    try:
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa")
    except:
        print("Ingresa solo números enteros")
    
print("\nProducto registrado:")
print("nombre:", nombre)
print("precio", precio)
print("Cantidad", cantidad)