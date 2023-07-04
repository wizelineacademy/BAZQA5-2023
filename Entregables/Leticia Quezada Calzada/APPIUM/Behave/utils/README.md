# **PROYECTO  APPIUM**
Proyecto en app de  compras de ropa *Swag Labs*,  donde se validan escenarios bàsicos para la compra de un producto .

## Contenidos
Este proyecto contiene algunos escenarios de Swag Labs, los casos de prueba son :
- *Login*: Donde se validan las credenciales validas del cliente
- *Products*: Donde se compara el Nombre y Precio de un articulo seleccionado
- *Buy products*: Donde se agrega al carrito un producto y se compara Nombre y Precio
- *Filter products*: Donde se ordenan los productos de menos a mayor y se recorre toda la vista para comparar el ùltimo articulo de la lista.

### Herramientas utilizadas
- flake8
- allure
- python 3.11
- Appium server
- Gherkins
- Appium inspector
- Behave
  
### Instalaciòn
Instalar las librerias del archivo requirements.txt

### Correr Prueba
- Comando general : behave features/
- Comando individual: behave features/login.feature 

### Configurar prueba
- Comando para ejecutar tags: behave --tags=@Nombre_tag

