Feature: final cucumber


  @Priority-High
  Scenario: Ingresar Usuario y Contrasena
    Given el sistema está en la pantalla de inicio
    When ingreso "Admin" como usuario
    And ingreso "fingsW2023" como contraseña
    Then debería permitir el acceso al sistema

  @Priority-High
  Scenario: Visualizar inventario
    Given estoy autenticado en el sistema
    When selecciono la opción de mostrar inventario
    Then debería mostrar una lista con todos los productos registrados en el inventario

  @Priority-Medium
  Scenario: Ingresar productos de manera satisfactoria
    Given estoy autenticado en el sistema
    When ingreso un nuevo producto con registro "123", nombre "Producto A", cantidad "10" y costo "15.99"
    Then el producto debería ser agregado al inventario
    And debería aparecer en la lista de inventario

  @Priority-High
  Scenario: Entrada y salida de productos
    Given estoy autenticado en el sistema
    And hay un producto con registro "123" en el inventario con cantidad "10"
    When selecciono la opción de reducir cantidad de productos
    And ingreso "123" como registro del producto
    And ingreso "5" como cantidad a reducir
    Then la cantidad del producto en el inventario debería ser "5"
    When selecciono la opción de agregar cantidad a un producto
    And ingreso "123" como registro del producto
    And ingreso "3" como cantidad a agregar
    Then la cantidad del producto en el inventario debería ser "8"
