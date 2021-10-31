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


class Scraping():
    def __init__(self, myDriver):
        self.driver=myDriver
        self.paginadores="/html/body/div[1]/div[2]/div[3]/div[4]/ul[2]/li[*]/a"
        self.lista_paginas=[]
        self.grilla_de_resultados='//*[@id="__next"]/div[2]/div[3]/div[4]/ul[1]/li[*]/article/a/div/div/span'
        self.cantidad_resultados_busqueda="/html/body/div[1]/div[2]/div[3]/div[3]/div[1]/span"
        self.chequear_marca="/html/body/div[1]/div[2]/div[3]/div[3]/div[3]/div[2]/span"
        self.breadcrumb_aparato="/html/body/div[1]/div[2]/div[3]/div[1]/div/ol/li[5]/span"               
                
    def get_traigo_marca_elegida(self):  
        marca_testing=self.driver.find_element(By.XPATH,self.chequear_marca).text
        return marca_testing
  
    def get_traigo_contenido_breadcrumb(self):
        breadcrumb_scrapping=self.driver.find_element(By.XPATH, self.breadcrumb_aparato).text
        return breadcrumb_scrapping
         
    def buscar_cant_paginas(self):
        paginador=self.driver.find_elements(By.XPATH,self.paginadores)
        for pagina in paginador:
          self.lista_paginas.append(pagina.text)
          #noto que el paginar+1 es el valor que debe entrar en el * de "/html/body/div[1]/div[2]/div[3]/div[4]/ul[2]/li[*]/a"
      
    def get_cantidad_resultados_busqueda_dom(self):
        #me trae del DOM el número de busquedas que registra el contador desarrollado por FrontEnd
        cantidad_items = self.driver.find_element(By.XPATH, self.cantidad_resultados_busqueda).text
        return cantidad_items

    def get_scraping(self, lista_grillas):
            #visito pagina por pagina y extraigo cantidad de heladeras por pagina
        for pagina in self.lista_paginas:
            time.sleep(3)
            #clickeo paginador por paginador a partir de 2da pagina
            self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div[4]/ul[2]/li["+str((int(pagina)+1))+"]/a").click()
            time.sleep(3)
            #tomo todos los div referentes a heladeras y los almaceno en grillas
            grillas=self.driver.find_elements(By.XPATH,self.grilla_de_resultados)
            for grilla in grillas:
                lista_grillas.append(grilla.text)
        return len(lista_grillas)


        
    
    
    


    
    

    
    
