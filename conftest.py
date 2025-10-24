import pytest
import tempfile
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    # Creamos opciones para el Chrome
    options = webdriver.ChromeOptions()

    # Sesion en modo incognito, impide pop-up de contraseña insegura
    options.add_argument("--incognito")

    # Definimos navegador con opciones cargadas
    driver = webdriver.Chrome(options=options)

    # Establecemos espera implicita gral
    driver.implicitly_wait(5)

    # Devolvemos el driver para utilizarlo
    yield driver

    # Luego de ejecutar tests, lo cerramos
    driver.quit()

@pytest.fixture
def login_with_driver(driver):
    login(driver)
    return driver