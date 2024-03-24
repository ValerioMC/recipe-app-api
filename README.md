# recipe-app-api

### Build docker image

docker build .

docker-compose build 

## Create project into our container

docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose run --rm app sh -c "django-admin startapp core"

## Run project

docker-compose up

## Update changes

docker-compose down
docker-compose build


## Run tests

docker-compose run --rm app sh -c "python manage.py test"