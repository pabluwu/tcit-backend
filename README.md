## Description

Prueba técnica para TCIT.

API REST escrita con Django Rest Framework

## Requirements

Python 3.11.3+

## Running the frontend app

```bash
#Crear ambiente virtual.
$ python -m venv env

#Activar ambiente virtual creado.
$ source env/bin/activate  

# En Windows usar.
$  env\Scripts\activate

# Instalar dependencias.
$ pip install -r requirements.txt

# Sincronizar BD.
$ python manage.py migrate

#Correr aplicación.
$ python manage.py runserver

```

## Consideraciones

- Por defecto en Settings.py viene la configuración a PostgreSQL con usuario postgres y clave admin.
- Viene agregado por defecto el cors para 'http://localhost:5173'