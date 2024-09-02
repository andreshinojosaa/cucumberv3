# features/steps/inventory_steps.py

from behave import given, when, then
from inventory import Producto, agregarProducto, buscarProductoPorRegistro, reducirCantidadProducto, mostrarInventario

@given('el sistema está en la pantalla de inicio')
def step_given_system_started(context):
    context.inventario = []

@given('estoy autenticado en el sistema')
def step_given_authenticated(context):
    context.autenticado = True

@when('ingreso un nuevo producto con registro {registro}, nombre "{nombre}", cantidad {cantidad:d} y costo {costo:f}')
def step_when_add_product(context, registro, nombre, cantidad, costo):
    producto = Producto(int(registro), nombre, cantidad, costo)
    agregarProducto(context.inventario, producto)

@then('el producto debería ser agregado al inventario')
def step_then_product_in_inventory(context):
    assert len(context.inventario) > 0, "El producto no se agregó correctamente."

@then('debería aparecer en la lista de inventario')
def step_then_product_in_list(context):
    registro = context.inventario[-1].registro
    productos = [p for p in context.inventario if p.registro == registro]
    assert len(productos) > 0, "El producto no aparece en la lista de inventario."

@when('selecciono la opción de reducir cantidad de productos')
def step_when_select_reduce(context):
    context.opcion_seleccionada = "reducir"

@when('ingreso "{registro}" como registro del producto')
def step_when_input_register(context, registro):
    context.registro = int(registro)

@when('ingreso "{cantidad:d}" como cantidad a reducir')
def step_when_input_reduce_quantity(context, cantidad):
    reducirCantidadProducto(context.inventario, context.registro, cantidad)

@then('la cantidad del producto en el inventario debería ser "{cantidad:d}"')
def step_then_verify_quantity(context, cantidad):
    producto = next((p for p in context.inventario if p.registro == context.registro), None)
    assert producto is not None, "El producto no fue encontrado."
    assert producto.cantidad == cantidad, f"Se esperaba {cantidad}, pero el producto tiene {producto.cantidad}."
