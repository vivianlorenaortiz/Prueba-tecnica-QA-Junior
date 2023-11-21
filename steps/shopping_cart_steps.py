from behave import given, when, then
from pages.login_page import LoginPage
from pages.shopping_cart_page import ShoppingCartPage
from utils.webdriver import WebDriver
from utils.url_base import Environment

@given('que el usuario "{user}" con la contraseña "{password}" tengo mas de un producto en el carro de compras')
def step_impl(context, user, password):
    context.driver = WebDriver().get_driver()
    context.login_page = LoginPage(context.driver)
    context.shopping_cart_page = ShoppingCartPage(context.driver)
    context.driver.get(Environment.BASE_URL)
    context.login_page.enter_username(user)
    context.login_page.enter_password(password)
    context.login_page.click_login_button()
    context.shopping_cart_page.click_add_product()
    context.shopping_cart_page.click_go_to_cart()
    context.shopping_cart_page.click_go_to_checkout()
    context.shopping_cart_page.enter_first_name("Usuario")
    context.shopping_cart_page.enter_last_name("Prueba")
    context.shopping_cart_page.enter_postal_code("110221")
    context.shopping_cart_page.click_continue_button_checkout()
    assert "43.18" in context.shopping_cart_page.get_total_price()
    context.shopping_cart_page.click_cancel_button()
    context.shopping_cart_page.click_go_to_cart()


@when("elimino un producto del carrito")
def step_impl(context):
    context.shopping_cart_page.click_remove_one_product()
    context.shopping_cart_page.click_go_to_checkout()
    context.shopping_cart_page.enter_first_name("Usuario")
    context.shopping_cart_page.enter_last_name("Prueba")
    context.shopping_cart_page.enter_postal_code("110221")
    context.shopping_cart_page.click_continue_button_checkout()


@then("el producto deberia ser eliminado y el total de la compra deberia actualizarse")
def step_impl(context):
    assert context.shopping_cart_page.display_checkout(), "El modulo de proceso de pago no está visible."
    assert "Checkout: Overview" in context.shopping_cart_page.get_title_module()
    assert "32.39" in context.shopping_cart_page.get_total_price()

    context.driver.quit()


