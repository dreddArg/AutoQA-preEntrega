#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):

    # Apertura Web
    driver.get("https://www.saucedemo.com/")

    # Espera explícita para comenzar a ingresar los datos
    username_textbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
    
    # Ingreso de datos y Login
    username_textbox.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()