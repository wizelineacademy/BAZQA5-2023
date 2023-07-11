# APPIUM

# Prueba de login, detalle de producto, ordenamiento de menor a mayor por precio del producto y compra del primer producto

Este proyecto contiene la automatización de casos de prueba del modulo de login,productos,el detalle de productos agregar el producto al carrito y la compra completa.
Para eso es necesario considerar la instalación de las siguientes herramientas de software.

* Python3
* Appium server
* Appium inspector
* IDE Pycharm community considerando la instalación de paquetes.
    * Appium-Python-client
    * Pytest
    * Flake8
    * Allure 
  
Agregar el capabilitie de acuerdo a las caracteriticas de dipositivo agrego imagen de refrencia y el json de ejemplo:
  
```bash
{
        "platformName": "android",
        "platformVersion": "10",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity",
        "appName": "Swag Labs Mobile App"

    }
```
Nota: `platform_version` y `device_name` depende del modelo de dipositivo android a utilizar y en `app` modificar la ruta de la app acorde al path en la que se encuentre el proyecto descargado ya que la ruta que se muestra cambia acorde al dispositivo que se esta usando

## enviroment.py

Se deben configurar de manera similar las capability en el archivo enviroment que es de donde se
toman las capability y deben corresponder al dispositivo que se esta usando.

Nota: `platform_version` y `device_name` depende del modelo de dipositivo android a utilizar y en `app` modificar la ruta de la app acorde al path en la que se encuentre el proyecto descargado ya que la ruta que se muestra cambia acorde al dispositivo que se esta usando


Una vez generado el capabilitie
* Guardar el capabilitie
* Iniciar el servidor de appium 
* estaras list@ para correr el proyecto


### Configuración del proyecto antes de correr el set de pruebas

Considerar los siguientes requerimientos [requirements.txt](requirements.txt)

Para instalar las dependencias utilizar el siguiente comando
  
 ```bash
pip install -r requirements.txt
``` 

## Set de pruebas

Para correr el set de pruebas debe tener la siguiente configuración 

* Se creo un una configuracion de ejecucion son el nombre: "Ejecucion" que ejecuta todos los casos de prueba

dentro del campo parameter colocar lo siguiente ya que en los feature tiene configurado el tag regression y los demas tags hacen referencia a la herramienta allure que le indica el formato que debe tomar para visualizar el reporte de la ejecucion

* ```bash
  --tags=regression
    -f
    allure_behave.formatter::AllureFormatter
    -o
    reports/android
    -f
    pretty
  ```  
  
## ¿Como lo hago?

Se accede a esa configuracion desde este menu:

![img.png](img/img.png)

En parameters agregar los siguientes tags

![img_1.png](img/img_1.png)

y se debe seleccionar la opcion "module name" apuntando al directorio behave del proyecto

![img.png](img/confi.png)

![img.png](img/directorio.png)

El working directory debe apuntar al directorio Behave del proyecto

![img.png](img/workin.png)

listo al dar tap en el boton para correr ejecutarias los casos de prueba


