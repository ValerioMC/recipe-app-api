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

    docker-compose run --rm app sh -c "python manage.py test && flake8"

## Migrations

    docker-compose run --rm app sh -c "python manage.py makemigrations"

    docker-compose run --rm app sh -c "python manage.py wait_for_db_raw && python manage.py migrate"

## List docker volume

    docker volume ls

    docker volume rm <volume>
