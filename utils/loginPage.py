from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver):
    driver.get("https://www.saucedemo.com/")
    
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    contraseña = driver.find_element(By.ID, "password")
    contraseña.send_keys("secret_sauce")

    contraseña.send_keys(Keys.RETURN)
    
def login_invalido(driver):
    driver.get("https://www.saucedemo.com/")
    
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    contraseña = driver.find_element(By.ID, "password")
    contraseña.send_keys("")

    contraseña.send_keys(Keys.RETURN)