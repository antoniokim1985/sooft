from unittest import result
import requests
import json
import re
import pytest


queryParam="Lagunitas"
url="https://api.openbrewerydb.org/breweries/autocomplete"
query="?query="


#defino url según estructura de query del endpoint
url_para_query=url+query+queryParam

#realizo la petición
response=requests.get(url_para_query)

#parseo contenido 
json_response=json.loads(response.text)

#defino criterio de busqueda previamente establecido
regex="Lagunitas Brewing Co"

#realizo bucle para ver en id cuales cumplen con condicion y los meto en una lista
lista_cumplieron=[]
criterio_debusqueda1 = "name"

for li in json_response:
 x=re.search(regex,li[criterio_debusqueda1])
 if x:
  lista_cumplieron.append(li)


#utilizando el id del resultado del primer endpoint, solicito una petición con los resultados.
url2="https://api.openbrewerydb.org/breweries/"

criterio_debusqueda2="state"
regex2="California"
resultadofinal=[]



for li in lista_cumplieron:
    response2=requests.get(url2+li["id"])
    #parseo
    json_response2=json.loads(response2.text)
    #chequeo criterio establecido state=California
    x2=re.search(json_response2[criterio_debusqueda2],regex2)
    if x2:
      #guardo resultado en lista de resultado final
      resultadofinal.append(json_response2)

 
#realizo assert de los resultados finales
for i in resultadofinal:     
  def test_criterios():
    assert i["name"] == "Lagunitas Brewing Co"
    assert i["street"]=="1280 N McDowell Blvd"
    assert i["phone"] =="7077694495"
         