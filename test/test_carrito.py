from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def test_carrito(login_in_driver):
    try:
        driver = login_in_driver
        
        # Agregar un producto al carrito
        driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
        
        #verificar que el contador del carrito se actualizó
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert contador_carrito == "1", f"El contador del carrito no se actualizó correctamente. Se esperaba '1' pero se obtuvo '{contador_carrito}'"
        
        
        #Obtener el nombre y precio del primer producto del listado de productos para verificar que se agregó el producto correcto al carrito
        nombre_producto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
        precio_producto = driver.find_elements(By.CLASS_NAME, "inventory_item_price")[0].text
                
        #Ir al carrito y verificar que el producto agregado esté presente
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        
        # Verificar que el nombre del producto en el carrito sea el mismo que el nombre del producto en el listado de productos
        nombre_producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre_producto == nombre_producto_en_carrito, f"El producto agregado al carrito no es el mismo que se muestra en el carrito. Se esperaba '{nombre_producto}' pero se obtuvo '{nombre_producto_en_carrito}'"
        
        
        # Verificar que el precio del producto en el carrito sea el mismo que el precio del producto en el listado de productos
        precio_producto_en_carrito = driver.find_elements(By.CLASS_NAME, "inventory_item_price")[0].text
        assert precio_producto == precio_producto_en_carrito, f"El precio del producto en el carrito no coincide con el precio del producto en el listado. Se esperaba '{precio_producto}' pero se obtuvo '{precio_producto_en_carrito}'"
        
        
        
        # Verificar que el producto esté en el carrito
        productos_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos_en_carrito) > 0, "No se encontraron productos en el carrito."
        
        # Verificar que el producto tenga un boton de eliminar visible
        boton_eliminar = driver.find_element(By.CLASS_NAME, "cart_button")
        assert boton_eliminar.is_displayed(), "El botón de eliminar no está visible en el carrito."
        
        # Eliminar el producto del carrito
        boton_eliminar.click()
        
        # Verificar que el carrito esté vacío
        productos_en_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(productos_en_carrito) == 0, "El carrito no se vació después de eliminar el producto."
        
        # Verificar que sea visible el boton de continuar comprando
        boton_continuar_comprando = driver.find_element(By.ID, "continue-shopping")
        assert boton_continuar_comprando.is_displayed(), "El botón de continuar comprando no está visible en el carrito."
        
        
    except Exception as e:
        print(f"Error en test_carrito: {e}")
        raise
    
    finally:
        driver.quit()