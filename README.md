# Cost Accounting

## How to run

Start services

```
docker-compose up -d postgres mailhog

```

Apply migrations

```
docker-compose run app python manage.py migrate
```

Start app

```
docker-compose up app
```

## How to run locally


Activate virtual env:

```

pipenv shell

```

Install dependencies:

```

pipenv install

```

Start services:

```

docker-compose up -d postgres mailhog

```

Run migrations

```

python manage.py migrate

```

Create super user:

```

python manage.py createsuperuser

```

Run server:

```

python manage.py runserver

```

Django cron for sending email:

```

python manage.py runcrons

```

