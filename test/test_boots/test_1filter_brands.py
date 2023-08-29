# Ingresar a la web, buscar un Botín, elegir un Mercurial Superfly y luego elegir el talle 10,
# una vez que lo encuentra, agregar al carrito.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import allure
from allure_commons.types import AttachmentType
import pytest
import time
from global_functions.Global import functions_global
from global_functions.Login import login_functions


driver = webdriver.Chrome()
Url = "https://www.lovellsoccer.co.uk/"
t = 1
lf = login_functions(driver)
fg = functions_global(driver)

# Elements
boots_hp = "//a[@href='https://www.lovellsoccer.co.uk/football-boots']"
boots_nike = "//body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]"
show_boots = "//a[@id='pageLinkAll']"
boots_superfly = "//body/div[5]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[160]/a[1]"
boots_size = "//a[@id='s_10']"
stock_msg = "//div[contains(text(),'This option is out of stock')]"
other_boot = "//body/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/div[4]/div[1]/a[1]"
add_to_cart = "//a[@id='addToCartLink']"


def test_filter_nike():
    fg.open_page(Url, t)
    try:
        fg.click_xi("xpath", boots_hp, t)
        fg.click_xi("xpath", boots_nike, t)
        mercurial_filter = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Nike Mercurial Boots")))
        mercurial_filter.click()

        fg.click_xi("xpath", show_boots, t)
        fg.click_xi("xpath", boots_superfly, t)
        fg.click_xi("xpath", boots_size, t)

        # Si no hay talle, elegir otro botín
        if stock_msg.text == "This option is out of stock":
            fg.click_xi("id", add_to_cart, t)
            print("Se agrega al carro")
        else:
            print("No había talle")
            fg.click_xi("xpath", other_boot, t)
            print("Se elige otro botín")
            fg.click_xi("xpath", boots_size, t)
            fg.click_xi("id", add_to_cart, t)
    except:
        print("No había talle disponible en Nike Mercurial")











