from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_to_inventory(login_with_driver):

    try:
        # Usamos funcion login
        driver = login_with_driver   

        # Prueba de redireccionamiento a web inventario
        assert "/inventory.html" in driver.current_url, "No se realizo la redireccion a web de inventario."

        # Prueba de Clase title = "Products"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products"

        # Prueba de Title Pestaña = "Swag Labs"
        assert driver.title == "Swag Labs"

        # Mensaje de test exitoso
        print("Login y redireccion a web inventario exitosa.")


    except Exception as e:
        print(f"Error test_login: {e}")
        raise
    finally:
        driver.quit()