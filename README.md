# API de Películas

Este proyecto demuestra cómo crear una API sencilla(de juguete) usando
**Django** y **Django-Rest-Framework**.

Esta API se usa para manejar un base de datos sencilla, en la cual se
encuentran películas.


### Configuración del entorno

Es necesario tener instalado Python en el sistema. Este debe ser accesible
a través de la variable de entorno PATH. Los siguientes pasos puden ser
ejecutados dentro de un _entorno virtual_.

**Instalar las dependencias del proyecto:**

````shell script
pip install -r requirements.tx
python manage.py makemigrations
python manage.py migrate
````


### Ejecutar los tests

La ejecución del siguiente comando ejecutará todos los tests en *test*:

````shell script
python runtests.py
````


### Descripción de la API

**url:** /movie/  
**Métodos HTTP:**
* GET: Obtener películas.
  * **/movie/** para obtener todas la películas
  * **/movie/_{id_de_película}_/** para obtener una película por su id.

* POST: Insertar película.

* PUT: Actualizar pelíclua.

* DELETE: Eliminar película.
  * **/movie/_{id_de_película}_/** para eliminar una película po su id.



**url:** /movie/country/  
**Métodos HTTP:**

* GET: Para obtener las películas por país. Se usa el siguiente
`json` en la petición:
````json
{
    "country": "Cuba"
}
````

**url:** /movie/actor/  
**Métodos HTTP:**

* GET: Para obtener las películas en las que participa un actor.
Se usa el siguiente `json` en la petición:
````json
{
    "actor": "Tom Hanks"
}
````

**url:** /movie/director/  
**Métodos HTTP:**

* GET: Para obtener las películas que dirigió un director.
Se usa el siguiente `json` en la petición:
````json
{
    "director": "Roberto Benigni"
}
````

**url:** /movie/genre/  
**Métodos HTTP:**

* GET: Para obtener las películas de un género.
Se usa el siguiente `json` en la petición:
````json
{
    "genre": "Drama"
}
````

**url:** /movie/year/  
**Métodos HTTP:**

* GET: Para obtener las películas por rango de años.
Se usa el siguiente `json` en la petición:
````json
{
    "minimumYear": 1990,
    "maximumYear": 2007
}
````