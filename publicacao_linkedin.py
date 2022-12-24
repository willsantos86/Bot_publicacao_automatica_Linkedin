from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.support import expected_conditions as condicao_esperada
import random

# Iniciar o webdriver
def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=en-US', '--window-size=1300,1000',
                 '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1

    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

# Digitar com comportamento humano.
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


driver, wait = iniciar_driver()

# Encontrar o site do Linkedin
driver.get('https://www.linkedin.com/home')

# Clicar e digitar o login
campo_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@id='session_key']")))
usuario = 'willsantos.edf@gmail.com'
digitar_naturalmente(usuario, campo_usuario)
sleep(4)

# Clicar e digitar a senha
campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//input[@id='session_password']")))
senha = '#Willi@m86'
digitar_naturalmente(senha, campo_senha)
sleep(3)

# Clicar no campo entrar (login)
botao_login = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//button[@class='sign-in-form__submit-button']")))
sleep(3)
botao_login.click()
sleep(10)

# Clicar no campo publicação
botao_publicacao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//span[text()='Começar publicação']")))
botao_publicacao.click()

# Digitar mensagem para publicação
campo_publicacao = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//div[@aria-placeholder='No que você está pensando?']")))
publicacao = 'Digite sua publicação aqui!'
digitar_naturalmente(publicacao, campo_publicacao)
sleep(3)

# Clicar no botão de publicação
botao_publicar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, "//span[text()='Publicar']")))
botao_publicar.click()
sleep(5)