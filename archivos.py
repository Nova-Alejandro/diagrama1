import csv

def cargar_csv(ruta):
    productos_cargados = []
    errores = 0
    
    try:
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            # Validar encabezado
            campos_esperados = {'nombre', 'precio', 'cantidad'}
            if not campos_esperados.issubset(set(lector.fieldnames)):
                print("Error: El archivo no tiene las columnas requeridas (nombre, precio, cantidad).")
                return None, 0

            for fila in lector:
                try:
                   
                    if not fila['nombre'] or not fila['precio'] or not fila['cantidad']:
                        raise ValueError
                    
                    nombre = fila['nombre'].strip()
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos_cargados.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except (ValueError, KeyError):
                    errores += 1
                    
        return productos_cargados, errores

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta}")
    except UnicodeDecodeError:
        print("Error: El archivo debe tener codificación UTF-8.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    
    return None, 0
