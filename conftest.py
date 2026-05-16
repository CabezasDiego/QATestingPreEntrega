import pytest
from selenium import webdriver
from utils.loginPage import login, login_invalido

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
        
    driver = webdriver.Chrome(options=options)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
    
@pytest.fixture
def login_invalido_driver(driver):
    login_invalido(driver)
    return driver
    

    