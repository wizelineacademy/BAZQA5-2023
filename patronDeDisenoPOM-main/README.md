# Swaglabs app - base de framework de automatizacion de interfaz movil
### Author: Isabella Ojeda Nuñez

Este repo es un ejemplo de una base para un framework de pruebas con el siguiente stack:
- Python
- Pytest
- Appium
- Allure
- Flake8

### Comando de ejecucion
Desde la consola, en la carpeta principal del proyecto:

Para ejecutar los casos de prueba:
>> pytest

Para ejecutar el analizador de codigo estático:
>>flake8 nameOfFileToCheck.py

Para generar reporte de Allure
>>pytest --alluredir=<ruta a la carpeta de reportes> test.py

Para ver los resultados del reporte con el servidor de Allure
>>Allure serve ./report 

### Appium
Este framework utiliza Appium, por lo tanto necesitamos instalar Appium en la maquina 
donde sera ejecutado y estar seguros que el servidor esta corriendo. Para ello lo podemos hacer
a traves del framework o de forma manual con la terminal.

### Contributions
Este es un proyeccto que acepta contribuciones, solo debes seguir los estandares del proyecto
para mantener la esctructura del mismo.....<br/>
Crea un PR y el equipo lo aprobara en caso de ser aceptado.
