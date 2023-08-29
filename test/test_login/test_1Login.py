from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import AttachmentType
import pytest
import time
from global_functions.Global import functions_global
from global_functions.Login import login_functions


# Datos logueo
Url = "https://www.lovellsoccer.co.uk/"
username = "b4fagiano@hotmail.com"
password = "placido"

driver = webdriver.Chrome()
t = 1
lf = login_functions(driver)
fg = functions_global(driver)


def test_login():
    try:
        lf.login(Url, username, password, t)
        fg.screenshot("Logueo exitoso.1")
        print("Logueo exitoso")
    except:
        print("No se pudo loguear")