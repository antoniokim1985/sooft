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

class Main():
    def __init__(self, myDriver):
        self.driver=myDriver
        self.cierrepopup="/html/body/div[1]/div[1]/div[1]/button"
        self.input="/html/body/div[1]/div[2]/header/div[2]/form/fieldset/div[1]/input"
        self.buscar="/html/body/div[1]/div[2]/header/div[2]/form/fieldset/div[1]/button"
        
    def cerrar_pop_up(self):
        self.driver.find_element(By.XPATH, self.cierrepopup).click()
    
    def realizar_busqueda(self, busqueda):
        self.driver.find_element(By.XPATH, self.input).click()
        self.driver.find_element(By.XPATH, self.input).send_keys(busqueda)
        self.driver.find_element(By.XPATH, self.buscar).click()