from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_to_inventory(login_with_driver):

    try:
        # Usamos funcion login
        driver = login_with_driver   

        # Prueba de redireccionamiento a web inventario
        assert "/inventory.html" in driver.current_url, "No se realizo la redireccion a la web inventory.html"
        print("Login y redireccionamiento exitoso.")

        # Prueba de Clase title = "Products"
        assert driver.find_element(By.CLASS_NAME,"title").text == "Products", "No se encontró el subtitulo 'Products'"
        print("Sub Titulo 'Products' verificado.")

    except Exception as e:
        print(f"Error test_login: {e}")
        raise
    finally:
        driver.quit()