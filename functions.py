from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login():
    # Definimos navegador
    driver = webdriver.Chrome()

    # Establecemos espera implicita gral
    driver.implicitly_wait(5)

    # Apertura Web
    driver.get("https://www.saucedemo.com/")
    
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    return driver