import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    # Definimos navegador
    driver = webdriver.Chrome()

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