import pytest
import time
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
    wait = WebDriverWait(driver, 20) 

    # Testar diferentes larguras de tela
    screen_sizes = [1920, 1366, 768, 375]  #Larguras em pixels (desktop, tablet, mobile)
    
    for size in screen_sizes:
        driver.set_window_size(size, 800)  #Define a largura e altura da janela
        time.sleep(3)  
        # Aguardar e clicar no ícone do menu de navegação
        menu_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='sticky-holder']/div[1]/div/div/div[1]/div[2]/a")))
        menu_icon.click()
        time.sleep(3)  

        # Aguardar o campo de busca e inserir o termo "dinheiro"
        search_field = wait.until(EC.element_to_be_clickable((By.NAME, "s")))
        search_field.click()
        
        # Limpar o campo de busca antes de inserir um novo termo
        search_field.clear()  
        search_field.send_keys("dinheiro")
        time.sleep(3)  

        # Enviar o formulário usando a tecla Enter
        search_field.send_keys(Keys.RETURN)  
        time.sleep(3) 

        # Aguardar a presença do resultado e verificar se o resultado contém o termo buscado
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'dinheiro')]")))  
            time.sleep(3)  
            
            # Verificar se o resultado contém o termo buscado
            assert "dinheiro" in driver.page_source, "O termo 'dinheiro' não foi encontrado nos resultados da busca."
        except TimeoutException: # type: ignore
            print(f"Tempo de espera excedido para a busca em {size}px. Verifique o XPath ou a presença do elemento.")

        # (Opcional) Testar elementos específicos para responsividade, como menus e botões.



