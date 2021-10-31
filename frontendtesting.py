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
import re
import HtmlTestRunner

from POM.busqueda import *
from POM.main import *
from POM.scraping import *


url="https://www.fravega.com/"
busqueda="Heladera"
ordenmarca="1"
marca_testing=""
lista_grillas=[]
cantidad_items=""
breadcrumb_scrapping=""
palabra_breadcrumb="Heladeras" 
     

class Frontendtesting(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path=r"/usr/lib/chromium-browser/chromedriver")
    self.vars = {}
    self.driver.get(url)
    self.driver.set_window_size(1920, 1053)
  
  #Testeo
  def test_sooft_breadcrumb(self):
    #cierro pop up y realizo busqueda
    time.sleep(2)
    self.main=Main(self.driver)
    self.main.cerrar_pop_up()
    time.sleep(2)
    self.main.realizar_busqueda(busqueda)
    time.sleep(2)
    
    #aplico filtro heladera y aplico filtro marca(primera)
    self.busqueda=Busqueda(self.driver,ordenmarca)
    self.busqueda.filtrar_menu_izquierda()
    self.busqueda.filtro_orden_marca()
    
          
    #traigo breadcrumb
    self.scraping=Scraping(self.driver)
    breadcrumb_scrapping=self.scraping.get_traigo_contenido_breadcrumb()
  
    print(breadcrumb_scrapping)
  
    regexItem=breadcrumb_scrapping
    assert regexItem == palabra_breadcrumb 
  
  
  def test_sooft_nro_items(self):
    #cierro pop up y realizo busqueda
    time.sleep(2)
    self.main=Main(self.driver)
    self.main.cerrar_pop_up()
    time.sleep(2)
    self.main.realizar_busqueda(busqueda)
    time.sleep(2)
    
    #aplico filtro heladera y aplico filtro marca(primera)
    self.busqueda=Busqueda(self.driver,ordenmarca)
    self.busqueda.filtrar_menu_izquierda()
    self.busqueda.filtro_orden_marca()
    
    #recorro paginas y guardo en una lista única todos los webelements encontrados en cada una de las páginas (en lista_grillas)
    self.scraping=Scraping(self.driver)
    self.scraping.buscar_cant_paginas()
    nroItemsDOM=self.scraping.get_cantidad_resultados_busqueda_dom()
    cantidad_items=self.scraping.get_scraping(lista_grillas)
    
    nroItemsDOM=int(cantidad_items)
    
    assert cantidad_items==nroItemsDOM


  def test_sooft_marca(self):
    #cierro pop up y realizo busqueda
    time.sleep(2)
    self.main=Main(self.driver)
    self.main.cerrar_pop_up()
    time.sleep(2)
    self.main.realizar_busqueda(busqueda)
    time.sleep(2)
    
    #aplico filtro heladera y aplico filtro marca(primera)
    self.busqueda=Busqueda(self.driver,ordenmarca)
    self.busqueda.filtrar_menu_izquierda()
    self.busqueda.filtro_orden_marca()
    
    #traigo la marca que fue elegida y la lista de elementos
    self.scraping=Scraping(self.driver)
    self.scraping.buscar_cant_paginas()
    self.scraping.get_scraping(lista_grillas)
    marca_testing=self.scraping.get_traigo_marca_elegida()
    for li in lista_grillas:
      self.assertIn(marca_testing,li)
        
  def teardown_method(self, method):
    self.driver.quit()           


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes'))
    
    
    

