from functions import login
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(5)

    try:
        # Usamos funcion login
        driver = login()   

        # Prueba de redireccionamiento a web inventario
        assert "/inventory.html" in driver.current_url, "No se realizo la redireccion a web de inventario."

        # Mensaje de test exitoso
        print("Login y redireccion a web inventario exitosa.")


    except Exception as e:
        print(f"Error test_login: {e}")
        raise
    finally:
        driver.quit()