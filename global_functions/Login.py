from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import AttachmentType
import time
from global_functions.Global import functions_global as fg

# selectores XPATH
button_plg = "(//a[@href='https://www.lovellsoccer.co.uk/login'])[2]"
button_lg = "//button[contains(text(),'Log in')]"


class login_functions():
    def __init__(self, driver):
        self.driver = driver

    def login(self, Url, username, password, t):
        fg.open_page(self, Url, t)
        time.sleep(3)
        button_plg = WebDriverWait(self.driver, t).until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='https://www.lovellsoccer.co.uk/login'])[2]")))
        button_plg.click()
        print("Se hace click en ", button_plg)
        user = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-email')))
        user.send_keys(username)
        print("Se escribe el texto: ", username)
        time.sleep(t)
        passw = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-password')))
        passw.send_keys(password)
        print("Se escribe el texto: ", password)
        time.sleep(t)
        button_lg = WebDriverWait(self.driver, t).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log in')]")))
        button_lg.click()
        print("Se hace click en ", button_lg)
        fg.screenshot("Logueo correcto")
        print("Logueo correcto")
