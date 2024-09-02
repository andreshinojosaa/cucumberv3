# inventory.py

class Producto:
    def __init__(self, registro, nombre, cantidad, costo):
        self.registro = registro
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo

def agregarProducto(inventario, producto):
    inventario.append(producto)

def buscarProductoPorRegistro(inventario, registro):
    for producto in inventario:
        if producto.registro == registro:
            return producto
    return None

def reducirCantidadProducto(inventario, registro, cantidad):
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        producto.cantidad -= cantidad

def mostrarInventario(inventario):
    return inventario
