from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cart(login_with_driver):

    try:
        driver = login_with_driver

        # Obtenemos primer producto presentado por la web
        product1 = driver.find_element(By.CLASS_NAME, "inventory_item")
        product1_name = product1.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"Nombre Producto elegido: {product1_name}")

        # Hacemos click en boton para agregar producto al cart
        product1.find_element(By.TAG_NAME, "button").click()
        
        # verificamos el valor del bagde del cart
        assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1", "El badge del carrito no aumento a 1."
        print("Cart badge aumentó a 1.")
        
        # navegamos al cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # prueba si estamos en web del cart
        assert "/cart.html" in driver.current_url, "No se realizo la redireccion a la web cart.html"
        print("Redireccion a web cart.html correcta.")
        cart_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"Nombre Producto en cart: {cart_product_name}")

        # comprobamos nombre producto agregado con producto en cart
        assert product1_name == cart_product_name , "Los nombres del producto no son iguales."
        print("Nombre de producto agregado correcto.")

    except Exception as e:
        print(f"Error test_cart: {e}")
        raise
