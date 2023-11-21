from behave import given, when, then
from pages.login_page import LoginPage
from utils.webdriver import WebDriver
from utils.url_base import Environment

@given("estoy en la pagina de inicio de sesion")
def step_impl(context):
    context.driver = WebDriver().get_driver()
    context.login_page = LoginPage(context.driver)
    context.driver.get(Environment.BASE_URL)


@when('ingreso el "{user}" y la contraseña "{password}" haciendo click en el boton de inicio de sesion')
def step_impl(context, user, password):
    context.login_page.enter_username(user)
    context.login_page.enter_password(password)
    context.login_page.click_login_button()


@then("ver la pagina del inventario de productos")
def step_impl(context):
    assert context.login_page.display_inventory() ,"El modulo de productos no está visible."
    assert "Swag Labs" in context.driver.title
    assert "Products" in context.login_page.get_title_module()

    context.driver.quit()


