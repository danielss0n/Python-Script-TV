from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver

from time import sleep
import os

edge_path = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
options = webdriver.EdgeOptions()
options.binary_location = edge_path
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Edge(options=options)
driver.fullscreen_window()


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

singnUp = False


def wait_to_click(xpath, driver):
    WebDriverWait(driver, 999).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


LOGADO = False
def logar(driver):
    global LOGADO
    wait_to_click("//button[contains(@title, 'Entrar')]", driver); 
    wait_to_click("//div[contains(@aria-label, 'Entre com a conta')]", driver)
    driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("password123") 
    driver.find_element(By.XPATH, "//span[@id='submitButton']").click() 

 
def esperar_e_clicar(elemento_xpath):
    try:
        elemento = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.XPATH, elemento_xpath))
        )
        elemento.click()
    except TimeoutException:
        pass


def main():
    global singnUp
    global LOGADO

    if singnUp == False:
        driver.get("site.com/url")
        logar(driver)
        singnUp = True

    driver.get("https://app.powerbi.com/report1")
    esperar_e_clicar("//button[contains(@title, 'Entrar')]")
    sleep(30)

    diretorio = f"C:/Users/{os.getenv('username')}/Desktop/pdfs"
    arquivos_pdf = [f for f in os.listdir(f"{diretorio}") if f.endswith(".pdf")]

    for arquivo in arquivos_pdf:
        caminho_completo = os.path.join(f"{diretorio}", arquivo) 
        driver.get(caminho_completo)  
        sleep(50)

    driver.get("https://app.powerbi.com/report2")
    esperar_e_clicar("//button[contains(@title, 'Entrar')]")
    sleep(35)
    driver.get("https://app.powerbi.com/report3")
    esperar_e_clicar("//div[@class='slicer-dropdown-menu'][@aria-label='DEPTO']")
    esperar_e_clicar("//div[@class='slicerItemContainer'][@title='Depto Caldeiraria']")

    sleep(45) 

while True:
    try:
        main()
    except Exception as e:
        driver.refresh()
        main()