Feature: Proceso de pago

  Scenario: Como usuario quiero realizar una compra para pagar el producto
    Given que el usuario "standard_user" con la contraseña "secret_sauce" ha agregado productos al carrito
    When un usuario ingreso los datos de pago durante el checkout
    Then el sistema deberia confirmar la recepcion de la orden