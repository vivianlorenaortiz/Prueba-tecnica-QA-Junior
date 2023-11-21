from behave import given, when, then
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from utils.webdriver import WebDriver
from utils.url_base import Environment

@given('que el usuario "{user}" con la contraseña "{password}" ha agregado productos al carrito')
def step_impl(context, user, password):
    context.driver = WebDriver().get_driver()
    context.login_page = LoginPage(context.driver)
    context.payment_page = PaymentPage(context.driver)
    context.driver.get(Environment.BASE_URL)
    context.login_page.enter_username(user)
    context.login_page.enter_password(password)
    context.login_page.click_login_button()
    context.payment_page.click_add_product()
    context.payment_page.click_go_to_cart()
    context.payment_page.click_go_to_checkout()



@when("un usuario ingreso los datos de pago durante el checkout")
def step_impl(context):
    context.payment_page.enter_first_name("Usuario")
    context.payment_page.enter_last_name("Prueba")
    context.payment_page.enter_postal_code("110221")
    context.payment_page.click_continue_button_checkout()
    context.payment_page.click_finish_button()


@then("el sistema deberia confirmar la recepcion de la orden")
def step_impl(context):
    assert context.payment_page.display_checkout_complete(), "El modulo de proceso completo no está visible."
    assert "Checkout: Complete!" in context.payment_page.get_title_module()

    context.driver.quit()


