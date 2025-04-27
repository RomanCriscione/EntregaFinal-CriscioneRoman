Este proyecto es una aplicación web desarrollada con Django 5.2, donde podés gestionar autores, posts, categorías y enviar mensajes privados entre usuarios.

- Crear el entorno virtual
python -m venv venv

- Activar el entorno virtual
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

- Instalar las dependencias
pip install -r requirements.txt

- Aplicar las migraciones
python manage.py migrate

- Crear un superusuario
python manage.py createsuperuser

- Levantar el servidor
python manage.py runserver

Fomato esperado de la fechas:
AAAA-MM-DD

Funcionalidades principales
Crear, listar, editar y eliminar autores y posts.
Crear categorías para los posts.
Enviar y recibir mensajes privados entre usuarios registrados.
Sistema de autenticación (login, logout, registro).
Edición de perfil de usuario.

Tecnologías utilizadas
Python 3.13
Django 5.2
HTML5

Notas
El proyecto utiliza SQLite3 como base de datos por defecto.
Hay un archivo .gitignore que excluye el entorno virtual, base de datos y archivos innecesarios.
Recomendación: utilizar un entorno virtual para evitar conflictos de dependencias.

## Video de demostración

Podés ver el video donde explico el funcionamiento del proyecto en el siguiente enlace: 
https://youtu.be/HJRRkec5Iuc

Autor
Román Criscione