# Rules of Thumb

## Main requisites for macOS
We will need Docker and Docker-compose installed on our system.

Docker-desktop: From https://docs.docker.com/docker-for-mac/install/ Mind the CPU vendor of your machine (Presumably Intel).


## Tech stack

### Database & Backend
* `Mysql` v.8.0

* `FastAPI` Framework.

* `Pipenv` as a Packaging tool.


## Run the database and the backend in a docker
The first time we will run the following command, on the project's root
  folder, to *build* a local `base` image of the service.

  ```sh
  docker-compose build
  ```

  Once the image is built we can start it up by running, on the project's root
  folder, the following command:

  ```sh
  docker-compose up -d
  ```

### Create tables and fill the database

Establish a connection through a tool such as Workbench using the following properties:
- MYSQL_ROOT_PASSWORD=root
- MYSQL_USER=master
- MYSQL_PASSWORD=master_pass
- MYSQL_DATABASE=rule_of_thumb_mysql

Use the file db.sql to create and fill the database. 

### Backend API
The service will be available at <http://localhost:8000>. However, you can see automatic interactive API documentation (provided by Swagger UI) at http://127.0.0.1:8000/docs
or (provided by ReDoc) http://127.0.0.1:8000/redoc.