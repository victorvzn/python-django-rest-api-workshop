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
* [ ] 2. Creamos y activamos el entorno virtual
  ```bash
  python -m venv venv
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