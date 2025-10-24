from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory(login_with_driver):

    try:
        driver = login_with_driver

        # Compruebo el Título de la pestaña
        assert driver.title == "Swag Labs"

        # Obtenemos listado de productos presentados por la web
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # Comprobamos que el listado de productos sea superior a cero
        assert len(products) > 0, "Sin productos en página"
    
    except Exception as e:
        print(f"Error test_inventory: {e}")
        raise
    finally:
        driver.quit()