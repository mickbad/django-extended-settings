# README

## About

This sample project demonstrates how to use the Django Extended Settings. It is designed to run under the 2.1.1 stable version of Django.

## How to

The test project requires a working installation of Django and Django Extended Settings

```bash
$ pip install django-extended-settings

or

# make virtualenv
$ pipenv install
```

Then you can run a server :

```bash
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver --insecure

or

# use virtualenv
$ pipenv shell
(example-f41erT) $ python manage.py migrate
(example-f41erT) $ python manage.py createsuperuser
(example-f41erT) $ python manage.py runserver --insecure
```

Option ```--insecure``` is for static files in production mode (cf ```settings.d/production_settings.py``` with ```DEBUG = False```).

Test these urls:

- Home:  http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin



## See

Then you can change extended settings without change your ```settings.py``` in path ```hellodjango/settings.d```

To be applied, files must have this pattern : ```[NAME]_settings.py```

Inside files, all settings is known from ```settings.py``` and other ```[NAME]_settings.py``` (after reading)

