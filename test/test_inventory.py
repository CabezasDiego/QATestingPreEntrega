from selenium.webdriver.common.by import By
import pytest

@pytest.fixture

def driver_logged(login_in_driver):
    return login_in_driver

def test_inventory_title(driver_logged):
    # Verificar que el título de la página sea correcto
    titulo = driver_logged.title
    assert titulo == "Swag Labs", f"El título de la página es incorrecto. Se esperaba 'Swag Labs' pero se obtuvo '{titulo}'"
    
    
def test_productos_visibles(driver_logged):
    
    # Verificar que haya al menos un producto en el catálogo
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos en el catálogo."
       
    
def test_ui_elements(driver_logged):
    
    # Verificar que el botón del menú y el filtro de productos estén visibles
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    
    assert filtro.is_displayed(), "El filtro no está visible."
    assert menu.is_displayed(), "El botón del menú no está visible."
    
    # Verificar que cada producto tenga un título visible
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    for producto in productos:
        titulo = producto.find_element(By.CLASS_NAME, "inventory_item_name")

        assert titulo.is_displayed(), "Un producto no tiene título visible."
        assert titulo.text != "", "Un producto tiene el título vacío."

    # Verificar que cada producto tenga un precio y mayor que 0
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    for producto in productos:
        precio = producto.find_element(By.CLASS_NAME, "inventory_item_price")

        assert precio.is_displayed(), "Un producto no tiene precio visible."
        assert float(precio.text.replace("$", "")) > 0, "El precio de un producto no es válido."


