from asyncio import sleep
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://acidezmental.com.br')
    yield driver
    driver.quit()

def test_navegacao_abas(driver):
    # Criação de uma instância do WebDriverWait para esperas explícitas
    wait = WebDriverWait(driver, 10)
    
    # Localizar e interagir com as abas usando XPaths corretos
    aba1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-principal-1']/li[1]/a/span")))
    print("Texto da aba1:", aba1.text)  
    aba1.click()
    time.sleep(3)

    aba2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-principal-1']/li[2]/a/span")))
    print("Texto da aba2:", aba2.text) 
    aba2.click()
    time.sleep(3)

    aba3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-principal-1']/li[3]/a/span")))
    print("Texto da aba3:", aba3.text) 
    aba3.click()
    time.sleep(3)

    aba4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-principal-1']/li[4]/a/span")))
    print("Texto da aba4:", aba4.text) 
    aba4.click()
    time.sleep(3)
