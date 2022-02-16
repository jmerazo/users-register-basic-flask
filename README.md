# Registro básico de usuarios
El proyecto visualiza una pantalla inicial de registro con datos básicos del usuarios y también permite la visualización de los registros realizados.

### Pre-requisitos
Se requiere:
- Python 3.9

## Instalación
- Descargar python 3.9 desde https://www.python.org/downloads/release/python-3910/ y ejecutar el instalador, add al path y siguiente hasta finalizar.

## Comenzando
Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.
- git clone https://github.com/jmerazo/users-register-basic-flask
Para la ejecución del proyecto es necesario contar con un entorno virtual, de preferencia **pipenv**
Una vez instalado python se procede con la instalación de **pipenv** con el siguiente comando:
- pip install pipenv
Luego dentro de la carpeta del proyecto, se ejecuta el comando:
- pipenv install
De esta forma se tendra el entorno virtual del proyecto y la instalación de las dependencias.
Para activar el entorno virtual es necesario correr en la consola el comando:
- pipenv shell

## Ejecutando pruebas
Para levantar el servicio del proyecto, una vez activado el entorno virtual, se escribe en la consola:
- Python app.py
De esta forma ya se podra acceder a la url:
- localhost:5000

## Construido con
* Flask
* SQLite
* Python


Development server |
Run: python app.py |
Route: Navigate to localhost:5000