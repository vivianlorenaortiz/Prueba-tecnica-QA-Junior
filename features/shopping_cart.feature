Feature: Carrito de compras

  Scenario: Como usuario quiero eliminar un producto en el carrito de compras para disminuir el valor de compra
    Given que el usuario "standard_user" con la contraseña "secret_sauce" tengo mas de un producto en el carro de compras
    When elimino un producto del carrito
    Then el producto deberia ser eliminado y el total de la compra deberia actualizarse