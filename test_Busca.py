import pytest
import time  # Importar o módulo time para pausas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # Importar Keys para usar o Enter

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://acidezmental.com.br/")
    yield driver
    driver.quit()

def test_busca(driver):
    # Criação de uma instância do WebDriverWait para esperas explícitas
    wait = WebDriverWait(driver, 10)

    # Aguardar e clicar no ícone do menu de navegação
    menu_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sticky-holder']/div[1]/div/div/div[1]/div[2]/a")))
    menu_icon.click()
    time.sleep(3)  

    # Aguardar o campo de busca e inserir o termo "dinheiro"
    search_field = wait.until(EC.element_to_be_clickable((By.NAME, "s")))
    search_field.click()
    search_field.send_keys("dinheiro")
    time.sleep(3)  

    # Enviar o formulário usando a tecla Enter
    search_field.send_keys(Keys.RETURN)  # Envia a tecla Enter
    time.sleep(3)  

    # Aguardar a presença do resultado e verificar se o resultado contém o termo buscado
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'dinheiro')]"))) 
    time.sleep(3)  

    # Verificar se o resultado contém o termo buscado
    assert "dinheiro" in driver.page_source, "O termo 'dinheiro' não foi encontrado nos resultados da busca."


def test_busca_sem_digitar(driver):

# Criação de uma instância do WebDriverWait para esperas explícitas
    wait = WebDriverWait(driver, 10)

    # Aguardar e clicar no ícone do menu de navegação
    menu_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sticky-holder']/div[1]/div/div/div[1]/div[2]/a")))
    menu_icon.click()
    time.sleep(3) 

    # Aguardar o campo de busca e avanço sem digitar uma pesquisa
    search_field = wait.until(EC.element_to_be_clickable((By.NAME, "s")))
    search_field.click()
    search_field.send_keys("")
    time.sleep(3)  

    # Enviar o formulário usando a tecla Enter
    search_field.send_keys(Keys.RETURN) 
    time.sleep(3)  

    # Aguardar a presença do resultado e verificar se o resultado contém todos os posts
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '')]")))  
    time.sleep(3)  

    # Verificar se o resultado contém o termo buscado
    assert "" in driver.page_source, "O termo '' não foi encontrado nos resultados da busca."
    
def test_busca_inexistente(driver):    
    # Criação de uma instância do WebDriverWait para esperas explícitas
    wait = WebDriverWait(driver, 10)

    # Aguardar e clicar no ícone do menu de navegação
    menu_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sticky-holder']/div[1]/div/div/div[1]/div[2]/a")))
    menu_icon.click()
    time.sleep(3) 

    # Aguardar o campo de busca e pesquiso por algo inexistente
    search_field = wait.until(EC.element_to_be_clickable((By.NAME, "s")))
    search_field.click()
    search_field.send_keys("aquario de sp")
    time.sleep(3)

    # Enviar o formulário usando a tecla Enter
    search_field.send_keys(Keys.RETURN)  
    time.sleep(3)

    # Aguardar a presença do resultado e verificar se o resultado é Showing 0 results for your search
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'aquario de sp')]")))  
    time.sleep(3) 

    # Verificar se o resultado contém o termo buscado
    assert "aquario de sp" in driver.page_source, "O termo 'aquario de sp' não foi encontrado nos resultados da busca."
    
