# Test task: Uploading and processing files

A Django REST API that allows files to be uploaded to a server and then processed asynchronously using Celery.

## Tech stack

- Python 3.11.5
- Django 4.2.6
- Django Rest Framework 3.14.0
- Psycopg 2.9.9
- Redis 5.0.1
- Celery 5.3.14
- Pip

## Install&Run

Start web application and database in Docker

### Clone project

```commandline
git clone git@github.com:kolaxy/files-uploading-processing.git
```

### Cd into

```commandline
cd files-uploading-processing
```

### Build

```commandline
docker-compose build
```

### Up

```commandline
docker-compose up
```

# Rest API

## Upload file

`POST /upload/`

    

## Get list of files with processed status

`GET /files/`

    curl -i -H 'Accept: application/json' http://localhost:8000/files/
