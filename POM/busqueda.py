import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest



class Busqueda():
    def __init__(self, myDriver, ordenmarca):
        self.driver=myDriver
        self.filtro_heladeras="/html/body/div[1]/div[2]/div[3]/div[3]/div[3]/ul/li[1]/h4/a"
        self.orden="/html/body/div[1]/div[2]/div[3]/div[3]/div[3]/ul/li["+ordenmarca+"]/a"  #ultimo numero es el numero de orden de lista

    def filtrar_menu_izquierda(self):
        self.driver.find_element(By.XPATH, self.filtro_heladeras).click()
        time.sleep(3)
 
    def filtro_orden_marca(self):
        self.driver.find_element(By.XPATH, self.orden).click()
        time.sleep(3)

