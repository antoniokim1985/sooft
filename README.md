----------------------------------------------------
            NOTAS
----------------------------------------------------

Usé python ya que es el lenguaje con el que habitualmente trabajo. Puedo usar JS ya que tengo conocimientos de la misma, usando Jest y Chai en vez de Unitest y Pytest. Preferí usar mi lenguaje más hábil, pero quería aclarar que puedo hacerlo en JS (con un poco más de dificultad).

Para la ejecución de la misma se deben instalar:
pip https://pip.pypa.io/en/stable/installation/#

pip install python

pip install json

pip install pytest

pip install unittest

pip install selenium

pip install requests

pip install regex

pip install HtmlTestRunner


Se puede ver la siguiente estructura de archivos
----------------------------------------------------

backendtesting.py      #testeo de backend

frontendtesting.py     #testeo de frontend (orquestador de POM)

POM/                   

     L main.py           #POM referente a página main (de ingreso)
   
     L busqueda.py       #POM referente a proceso de navegación y búsqueda
   
     L scraping.py       #POM referente a scraping de datos para luego ser utilizados en frontendtesting
   
reportes/

       L Backendtesting.html                              #reporte que se genera automaticamente cuando ejecuto la prueba de back
       
       L Test_Results__main__Frontendtesting_~.html       #reporte que se genera automaticamente cuando ejecuto la prueba de front
       


----------------------------------------------------
EJECUCION

Dado que frontendtesting corre con Unitest (plataforma sobre la que se monta selenium)
Los reportes los realiza htmltestrunner
Para que genere el reporte, simplemente hay que poner "Run" al archivo frontendtest.py

Dado que backendtesting corre con Pytest
Los reportes los genera directamente pytest
Para ello, hay que correrlo poniendo el siguiente comando en la terminal (sobre el directorio)
pytest -v backendtesting.py --html=reportes/Backendtesting.html --self-contained-html

Se puede unificar?, si... puede realizar el testing de back con unitest.
Se puede realizar reportes en xml/json para que puedan impactar directo en un ambiente de CI/CD con la plataforma... sí, se puede, solo hay que cambiar de reporter

Reportes se pueden ver en directorio /reportes que se genera al realizar las pruebas.


----------------------------------------------------
FRONTENDTESTING

Breadcrumb testing: Tener en cuenta que breadcrumb no es igual a la palabra de busqueda.
Si yo cambio las palabras, es posible que surja un fallo ya que se realiza un assert de la palabra previamente informada por la consigna.
Se puede utilizar regex y hacerlo más flexible?. sí, pero no lo hice ya que no lo contempló la consigna.


----------------------------------------------------
BACKENDTESTING

Vease que no se pueden realizar muchas modificaciones ya que al realizarlas falla el testeo.
Esto se debe a que los datos a asegurar son datos dados por la consigna-
