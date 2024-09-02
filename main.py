# main.py

import os
import getpass
from inventory import Producto, agregarProducto, buscarProductoPorRegistro, reducirCantidadProducto, mostrarInventario, agregarCantidadProducto, eliminarProducto

def mostrarPantallaInicio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print("*********************************************************")
    print("*                                                       *")
    print("*        Bienvenido al Sistema de MYI                   *")
    print("*                                                       *")
    print("*             Presione cualquier tecla para continuar... *")
    print("*                                                       *")
    print("*********************************************************")
    input()  # Espera a que el usuario presione una tecla
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla después de la entrada

def mostrarEncabezado():
    print("\n\n")
    print("  __  ____   ______ ")
    print(" |  \\/  \\ \\ / /_ _| ")
    print(" | |\\/| |\\ V / | |")
    print(" | |  | | | |  | |")
    print(" |_|  |_| |_| |___|")
    print("\n")

def mostrarMenu():
    mostrarEncabezado()
    print("\n1. Agregar Producto")
    print("2. Buscar Producto por Registro")
    print("3. Mostrar Inventario")
    print("4. Reducir cantidad de productos existentes")
    print("5. Agregar cantidad a un Producto existente")
    print("6. Eliminar Producto")
    print("7. Salir")
    return int(input("Ingrese una opcion: "))

def existeRegistro(inventario, registro):
    return any(p.registro == registro for p in inventario)

def agregarProducto(inventario):
    registro = int(input("Ingrese numeral del producto: "))
    if existeRegistro(inventario, registro):
        print("Error: El registro del producto ya existe. No se puede agregar un producto con el mismo registro.")
        return

    nombre = input("Ingrese nombre del producto: ")
    cantidad = int(input("Ingrese cantidad del producto: "))
    costo = float(input("Ingrese valor del producto: "))
    producto = Producto(registro, nombre, cantidad, costo)
    agregarProducto(inventario, producto)

def buscarProductoPorRegistro(inventario, registro):
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        print(f"\nRegistro: {producto.registro}")
        print(f"Producto: {producto.nombre}")
        print(f"Cantidad: {producto.cantidad}")
        print(f"Costo: {producto.costo}")
    else:
        print("El producto no fue encontrado.")

def mostrarInventario(inventario):
    for producto in inventario:
        print(f"\nRegistro: {producto.registro}")
        print(f"Producto: {producto.nombre}")
        print(f"Cantidad: {producto.cantidad}")
        print(f"Costo: {producto.costo}")
        print("-----------------------------")

def iniciarSesion():
    usuario = input("Ingrese usuario: ")
    contrasena = getpass.getpass("Ingrese contrasena: ")
    if usuario == "Admin" and contrasena == "fingsW2023":
        return True
    else:
        print("Usuario o contrasena incorrectos. Acceso invalido.")
        return False

def reducirCantidadProducto(inventario, registro, cantidadAReducir):
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        if producto.cantidad >= cantidadAReducir:
            producto.cantidad -= cantidadAReducir
            print(f"Se han reducido {cantidadAReducir} unidades del producto {producto.nombre}")
        else:
            print(f"No hay suficientes unidades para reducir. Cantidad disponible: {producto.cantidad}")
    else:
        print("Producto no encontrado en el inventario.")

def agregarCantidadProducto(inventario):
    registro = int(input("Ingrese el registro del producto a incrementar: "))
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        producto.cantidad += cantidad
        print(f"Se han agregado {cantidad} unidades al producto {producto.nombre}")
    else:
        print("Producto no encontrado en el inventario.")

def eliminarProducto(inventario, registro):
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        inventario.remove(producto)
        print(f"Producto con registro {registro} eliminado exitosamente.")
    else:
        print(f"Producto con registro {registro} no encontrado.")

def caratula():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print("*********************************************************")
    print("*                                                       *")
    print("*        ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦        *")
    print("*        ¦                                     ¦        *")
    print("*        ¦        Contraseña Correcta!         ¦        *")
    print("*        ¦                                     ¦        *")
    print("*        ¦      Bienvenido al Sistema de       ¦        *")
    print("*        ¦       Gestión de Inventario         ¦        *")
    print("*        ¦                                     ¦        *")
    print("*        ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦        *")
    print("*                                                       *")
    print("*********************************************************")
    input("Presione cualquier tecla para continuar...")

def main():
    mostrarPantallaInicio()
    mostrarEncabezado()

    if not iniciarSesion():
        return
    
    caratula()
    os.system('cls' if os.name == 'nt' else 'clear')

    inventario = []
    opcion = 0

    while opcion != 7:
        opcion = mostrarMenu()

        if opcion == 1:
            agregarProducto(inventario)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 2:
            registro = int(input("Ingrese registro del producto a buscar: "))
            buscarProductoPorRegistro(inventario, registro)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 3:
            mostrarInventario(inventario)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 4:
            registro = int(input("Ingrese el registro del producto: "))
            cantidad = int(input("Ingrese la cantidad a reducir: "))
            reducirCantidadProducto(inventario, registro, cantidad)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 5:
            agregarCantidadProducto(inventario)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 6:
            registro = int(input("Ingrese el registro del producto a eliminar: "))
            eliminarProducto(inventario, registro)
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == 7:
            print("Saliendo del programa, ¡hasta pronto!")
        else:
            print("Opcion invalida, intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
