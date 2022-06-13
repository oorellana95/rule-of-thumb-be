# Rules of Thumb

## Main requisites for macOS
We will need Docker and Docker-compose installed on our system.

Docker-desktop: From https://docs.docker.com/docker-for-mac/install/ Mind the CPU vendor of your machine (Presumably Intel).


## Tech stack

### Database
* `Mysql` v.8.0

### Backend
* `FastAPI` Framework.

* `Pipenv` as a Packaging tool.


## Prepare the database
Install docker and run the following command on the terminal:
  ```sh
  docker run --name rule_of_thumb_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=master -e MYSQL_PASSWORD=master_pass -e MYSQL_DATABASE=rule_of_thumb_mysql mysql:8.0
  ```

Establish a connection through a tool such as Workbench using the following properties:
- MYSQL_ROOT_PASSWORD=root
- MYSQL_USER=master
- MYSQL_PASSWORD=master_pass
- MYSQL_DATABASE=rule_of_thumb_mysql

Finally, use the file db.sql to create and fill the database. 


## Run the backend in local
Install pipenv dependencies
  ```sh
  pipenv install
  ```

Run the backend using the following command:
  ```sh
  uvicorn project.main:app --reload
  ```


### Backend Interactive API docs
> You will see the automatic interactive API documentation (provided by Swagger UI) going to http://127.0.0.1:8000/docs
or (provided by ReDoc) in http://127.0.0.1:8000/redoc.