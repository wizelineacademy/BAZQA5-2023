
# Prueba de login

Este proyecto contiene la automatización de casos de prueba del modulo de login, productos, detalle de producto.
Para eso es necesario considerar la instalación de las siguientes herramientas de software.

* Python3
* Appium server
* Appium inspector
* IDE Pycharm community considerando la instalación de paquetes.
    * Appium-Python-client
    * Pytest
    * Flake8
    * Allure

## Python3
Entrar a la página oficial https://www.python.org/ y descargar de acuerdo al tipo de sistema operativo con el que se va a trabajar.  

## Appium server
Ingresar a la página oficial https://appium.io/downloads.html seleccionar Appium Desktop Apps mismo que direccionará a github para que descargue el ejecutable que corresponda a su sistema operativo.
Una vez instalado dejar los parametros por default Host y Port y oprimir el botón starServer como el que se muestra en la siguiente pantalla:
   
![img.png](img.png)  

## Appium inspector
Para instalar appium inspector es necesario ingresar a la siguiente url https://github.com/appium/appium-inspector/releases mima que direcciona al repositorio que tiene los ejecutables de acuerdo a cada tipo de sistema operativo.   
Una vez instaldo confirmar que se tenga el mismo host y port que en appium server y agregar en el campo path lo siguiente `/wd/hub`  
  
Agregar el capabilitie de acuerdo a las caracteriticas de dipositivo agrego imagen de refrencia y el json de ejemplo:  

![img_1.png](img_1.png)  
  
```bash
{
        'platformName': 'Android',
        'deviceName': '56295fdf',
        'app': 'e:/Users/948255/Documents/CursoWizelineAutomation/Entregables/APPIUM/APP/sauce_app.apk',
        'appPackage': 'com.swaglabsmobileapp',
        'appActivity': '.MainActivity'

    }
```
Una vez generado el capabilities
* Guardar el capabilities
* Iniciar la sesión
* Es necesario iniciar appium

![img_2.png](img_2.png)

## IDE Pycharm Community
Ingresar a la página oficial https://www.jetbrains.com/es-es/pycharm/ y descargar el
ejecutable Community. Recuerde que durante la instalación se deben ambientar las variables de entorno.
El mismos ejecutable presenta una pantalla que permite la configuración de las variables de entorno. 

Una vez que se tenga el IDE, instalar los siguientes paquetes con el uso de la terminal.  
Nota: es importante antes instalar nodeJS para ejecutar los comandos con el prefijo npm. 


### Importar proyecto dentro del IDE
* Oprimir el menu File
* De la lista desplegada oprimir el botón Open
* Buscar el proyecto y oprimir la opción abrir


### Configuración del proyecto antes de correr el set de pruebas

Considerar los siguientes requerimientos [requirements.txt](requirements.txt)

Para instalar las dependencias utilizar el siguiente comando
  
 ```bash
pip install -r requirements.txt
``` 

Dentro de la carpeta Behave/utils/dictionaries encontrará un archivo input_data.py que contiene las credenciales para poder realizar un login en la app de prueba, las credenciales se las proporcionará negocio.
```bash
STANDARD_USER=
PASSWORD=
```

## Set de pruebas

Para correr el set de pruebas debe tener la siguiente configuración 

* home test que ejecutaría todos los casos de prueba
![img_3.png](img_3.png)
dentro del campo parameter colocar lo siguiente
* ```bash
  --tags=regression
  -f
  allure_behave.formatter::AllureFormatter
  -o
  reports/android
  -f
  pretty
  features/
  
  
  ```  
  Nota: ``device_name` depende del dipositivo android a utilizar, esto se puede consultar con el comando

* adb devices

### Para pruebas de regresion 
* Tener una nueva configuración en este caso se nombró regression
* Agregar el parametro `--tags=regression`  

### Pruebas de humo
* Tener una nueva configuración en este caso se nombró smokeTest
* Agregar el parametro `--tags=smoke`  

Cada nuevo tag o etiqueta del tipo de prueba se debe colocar en los features especificamente en la parte superior del escenario(Scenario)  
![img_6.png](img_6.png)
  
### Reportes Allure  

Para generar reporte con Allure, es necesario abrir el archivo Beheve/environment.py y quitar el comentario a la linea:

* subprocess.run("allure serve reports/android", shell=True)
