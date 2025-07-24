# Taller: Crea tu primera API REST con Python y Django

* Bootcamp: Desarrollo Web FullStack con Python Elearning
* Temas: Python, Django, API Rest

### TODO 

* [ ] 0. Clonar el repositorio base del taller
  ```bash
  git clone https://github.com/victorvzn/python-django-rest-api-workshop.git
  cd python-django-rest-api-workshop
  ```
* [ ] 1. Verificamos que tenemos Python instalado
  ```bash
  python --version
  ```
* [ ] 2. Creamos el entorno virtual para python, activamos e instalamos las dependencias de Python y Django
  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
* [ ] Ahora generemos la primera migracion que incluye el modelo Banda
  ```bash
  python manage.py migrate
  ```
* [ ] Ahora cargamos los datos de prueba para el modelo Banda y el modelo auth.users con un usuario de prueba
  ```bash
  python manage.py loaddata bandas.json
  ```
* [ ] Ahora podemos iniciar el servidor de desarrollo
  ```bash
  python manage.py runserver
  ```
* [ ] Ahora podemos acceder a la parte administrativa de Django con las credenciales
  **username: admin / password: admin**
  ```bash
  http://127.0.0.1:8000/admin/
  ```

  ## Links

  * [Django](https://www.djangoproject.com/)
  * [Django REST Framework](https://www.django-rest-framework.org/)
  * [Python](https://www.python.org/)
     
  | Docente: Victor Villazón - Julio 2025
