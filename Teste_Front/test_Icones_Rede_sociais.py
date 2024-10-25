import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://acidezmental.com.br/")
    yield driver
    driver.quit()

def test_redes_sociais(driver):
    social_links = {
        "Twitter": ".footer-social-list > .social-link-twitter > .rbi",
        "Pinterest": ".footer-social-list > .social-link-pinterest > .rbi",
        # Adicione mais redes sociais conforme necessário
    }

    time.sleep(5)  # Espera de 5 segundos na tela principal antes de clicar

    # Rolagem até o final da tela principal
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Espera para visualizar a rolagem

    for index, (name, selector) in enumerate(social_links.items()):
        click_social_link(driver, selector, name)
        if index == 0:  # Se for o primeiro link, feche o navegador
            driver.quit()  # Fecha o navegador
            time.sleep(2)  # Espera antes de reabrir
            driver = reopen_browser()  # Reabre o navegador
            driver.get("https://acidezmental.com.br/")  # Retorna à página inicial
            time.sleep(5)  # Espera de 5 segundos após reabrir o navegador

            # Rolagem até o final da tela principal novamente
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Espera para visualizar a rolagem

def click_social_link(driver, selector, name):
    try:
        # Clicar no ícone da rede social
        link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        link.click()

        # Esperar pela nova janela
        time.sleep(7)  # Espera breve para visualizar a mudança de janela
        wait_for_new_window(driver)

        # Verificar se a nova janela está correta
        new_window = driver.window_handles[-1]  # Última janela aberta
        driver.switch_to.window(new_window)
        print(f"Verificando URL da {name}...")
        WebDriverWait(driver, 10).until(EC.url_contains(name.lower()))  # Verificar se a URL contém o nome da rede
        print(f"A URL da {name} foi carregada com sucesso: {driver.current_url}")

        # Voltar à janela anterior
        driver.close()  # Fechar a janela atual
        driver.switch_to.window(driver.window_handles[0])  # Voltar para a janela original
    except Exception as e:
        print(f"Erro ao testar o link do {name}: {str(e)}")

def reopen_browser():
    driver = webdriver.Chrome()  # Cria uma nova instância do navegador
    driver.maximize_window()  # Maximiza a janela
    return driver

def wait_for_new_window(driver, timeout=10):
    WebDriverWait(driver, timeout).until(lambda d: len(d.window_handles) > 1)




