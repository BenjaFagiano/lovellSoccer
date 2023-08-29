from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import AttachmentType



class functions_global():
    def __init__(self, driver):
        self.driver = driver


    def open_page(self, Url, tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        print("Se abre la web: ", Url)
        t = time.sleep(tiempo)

        #zoom_script = "document.body.style.zoom = '100%"
        #self.driver.execute_script(zoom_script)
        #return Url

    # Encontrar elemento por XPATH
    def FEX(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    # Encontrar elemento por ID
    def FEI(self, elemento):
        val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val


    def texto_xi(self, tipo, selector, texto, tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Se escribe: ", texto)
                t = time.sleep(tiempo)
                return val
            except TimeoutException as ex:
                print("No se encuentra el elemento: ", selector)
                return val
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Se escribe: ", texto)
                t = time.sleep(tiempo)
                return val
            except TimeoutException as ex:
                print("No se encuentra el elemento: ", selector)
                return val


    def click_xi(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("Damos click en el botón: ", selector)
                t = time.sleep(tiempo)
                return val
            except TimeoutException as ex:
                print("No se encuentra el elemento: ", selector)
            return val
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("Damos click en el botón: ", selector)
                t = time.sleep(tiempo)
                return val
            except TimeoutException as ex:
                print("No se encuentra el elemento: ", selector)
                return val


    def screenshot(self, nombre):
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type = AttachmentType.PNG)


