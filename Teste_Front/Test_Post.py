import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="function")
def driver():
    # Inicializa o Chrome WebDriver
    driver = webdriver.Chrome()
    driver.set_window_size(1936, 1056)
    yield driver
    driver.quit()

def test_abrir_posts(driver):
    driver.get("https://acidezmental.com.br/")
    
    # Clicar na postagem destacada
    clicar_postagem_destacada(driver)

    # Acessar os links da postagem
    acessar_links_da_postagem(driver)

def clicar_postagem_destacada(driver):
    try:
        # Espera até que o elemento esteja clicável e clica
        postagem_destacada = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".block-inner > .p-highlight .overlay-inner"))
        )
        postagem_destacada.click()
        time.sleep(5)  # Espera para visualizar a postagem
    except Exception as e:
        print(f"Erro ao clicar na postagem destacada: {str(e)}")

def acessar_links_da_postagem(driver):
    # Selecionar os links das postagens
    links = [
        ".p-grid:nth-child(1) .p-url",
        ".p-grid:nth-child(3) .p-url"
    ]

    for link_selector in links:
        try:
            # Rolagem até o elemento
            scroll_para_elemento(driver, link_selector)

            # Espera até que o elemento esteja clicável e clica
            link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, link_selector))
            )
            link.click()
            time.sleep(5)  # Espera para visualizar a nova página

            # Voltar à página anterior após visualizar o link
            driver.back()  
            time.sleep(2)  # Espera para garantir que a página anterior carregou
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".block-inner > .p-highlight .overlay-inner")))  # Aguarda a postagem anterior
        except Exception as e:
            print(f"Erro ao clicar no link: {link_selector}: {str(e)}")

def scroll_para_elemento(driver, selector):
    try:
        # Executa a rolagem até o elemento
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)  # Breve pausa para visualizar o scroll
    except Exception as e:
        print(f"Erro ao rolar para o elemento: {selector}: {str(e)}")
