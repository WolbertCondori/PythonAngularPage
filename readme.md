# Django

### Comando para crear un venv o .venv
- [Python o Python3] -m -venv {NombreVenv}[venv o .venv]
- Windows:
  - .\[venv o .venv]\Scripts\active
- Linux:
  - source ./venv/[bin o lib]/active

### Crear Proyecto Django
- Primero comprobamos que [venv o .venv] se está activo en la terminal.
- pip: usamos esta herramienta para instalar dependencias
  - pip install django
    - Esto nos creará la carpeta de configuración y manage.py
  - Creamos assets/static, assets/media, templates, y .env.
  - Configuramos

### Comandos que se usan en un proyecto

- django-admin startproject NombreProyecto (Recordad que para ejecutar esto hay que instalar django)
    - pip install django
    - pip install python-decouple (Librería para leer variables secretas en archivos .env)
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- python manage.py createsuperuser
- python manage.py startapp NombreApp

### Comandos para iniciar el proyecto
Para iniciar este proyecto:
1. Creamos venv
2. Entramos en el venv.
3. Nos posicionamos en la carpeta Raiz, donde está .env, requirements.txt, etc
4. escribimos:
- pip install -r requirements.txt