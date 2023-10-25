# Test task: Uploading and processing files

A Django REST API that allows files to be uploaded to a server and then processed asynchronously using Celery.

## Tech stack

- Python 3.11.5
- Django 4.2.6
- Django Rest Framework 3.14.0
- Psycopg 2.9.9
- Redis 5.0.1
- Celery 5.3.14
- Flower 2.0.1
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
docker compose build
```

### Up

```commandline
docker compose up
```

# Rest API
    
## Get list of files with processed status

`GET /files/`

    curl -i -H 'Accept: application/json' http://localhost:8000/files/

    HTTP/1.1 200 OK
    Date: Wed, 25 Oct 2023 11:13:26 GMT
    Server: WSGIServer/0.2 CPython/3.11.5
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 2
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin

    []


## Upload file

`POST /upload/`

    curl -i -X POST -F "file=@/pathToYourFile" http://localhost:8000/upload/

    HTTP/1.1 201 Created
    Date: Wed, 25 Oct 2023 11:16:37 GMT
    Server: WSGIServer/0.2 CPython/3.11.5
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 53
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin
    Cross-Origin-Opener-Policy: same-origin

    {"file":"http://localhost:8000/media/production.yml"}


# Track tasks

## Flower 

You can track celery tasks by Flower

`http://localhost:5555/`

![Alt text](flower.png)