from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_validation(login_in_driver):
    try:
        #test de login exitoso
        driver = login_in_driver    
        
        assert "/inventory" in driver.current_url, "No se redirigió a la página de inventario después del inicio de sesión exitoso."
        
    except Exception as e:
        print(f"Error en test_login_validation: {e}")
        raise
    
    finally:
        driver.quit()

def test_login_invalido(login_invalido_driver):
    try:
        #test de login fallido
        driver = login_invalido_driver
        mensaje_error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        
        assert mensaje_error.is_displayed(), "No se redirigió a la página de inicio de sesión después del intento fallido."
        
    except Exception as e:
        print(f"Error en test_login_invalido: {e}")
        raise
    
    finally:
        driver.quit()