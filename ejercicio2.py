productos = [{"codigo": 10, "nombre": "Mando PS5", "precio": 34990, "stock": 4},
              {"codigo": 11, "nombre": 'Monitor AOC 24"', "precio": 74990, "stock": 2},
              {"codigo": 12, "nombre": 'Teclado mecánico RedDragon', "precio": 28990, "stock": 5},
              {"codigo": 13, "nombre": 'Mouse gamer RGB RAZER', "precio": 22990, "stock": 8},
              {"codigo": 14, "nombre": 'NoteBook ASUS 18" Intel-Core', "precio": 253990, "stock": 1}]

def buscar_producto(productos, codigo):
    print("BUSCAR PRODUCTOS")
    for producto in productos:
        if producto["codigo"] == codigo:
            print("El producto si existe en el inventario.")
            return producto
    print("El producto no existe en el inventario.")
    return None 

def mostrar_productos(producto):
    if producto:
        print(producto)
    else:
        print("No se encontró el producto.")

id_producto = int(input("Ingrese el código del producto a buscar: "))
producto = buscar_producto(productos, id_producto)
mostrar_productos(producto)