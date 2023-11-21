Feature: Ingreso de usuarios

  Scenario Outline: Como usuario quiero realizar el login para acceder al Home
    Given estoy en la pagina de inicio de sesion
    When ingreso el "<User>" y la contraseña "secret_sauce" haciendo click en el boton de inicio de sesion
    Then ver la pagina del inventario de productos

    Examples:
      | User       |
      | standard_user       |
      | problem_user       |
      | performance_glitch_user |
      | visual_user    |