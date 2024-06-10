from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://advantageonlineshopping.com/#/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_Login(driver):
    perfil = driver.find_element(By.ID, "menuUserSVGPath")
    perfil.click()    
    sleep(3)
    
    username = driver.find_element(By.NAME, "username")
    username.send_keys("FlavioSilva")
    
    password = driver.find_element(By.NAME, "password")
    password.send_keys("1234Abc")
    sleep(3)
    
    button = driver.find_element(By.ID, "sign_in_btn")
    button.click()
    sleep(10)
    
    lupa = driver.find_element(By.ID, "menuSearch")
    lupa.click()
    sleep(3)  
    
    autocomplete = driver.find_element(By.ID, "autoComplete")
    autocomplete.send_keys("HP Chromebook 14 G1(ENERGY STAR)") 
    sleep(8) 
    
    produto = driver.find_element(By.XPATH, "//header//div/div[2]/a[2]/p")
    produto.click()
    sleep(3)
    
    button = driver.find_element(By.NAME, "save_to_cart")
    button.click()
    
    carrinho = driver.find_element(By.ID, "menuCart")
    carrinho.click()
    sleep(5)
    
    total = driver.find_element(By.XPATH, "//tfoot//tr//td[2]//span").text
    total = total.split("$")[1]
    total = float(total)
    
    # Valide o valor do produto aqui
    valor_esperado = 299.99
    assert total == valor_esperado, f"Valor do produto não corresponde. Esperado: ${valor_esperado}, Encontrado: ${total}"
    sleep(10)
