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

Then you can run a server to test http://127.0.0.1:8000

```bash
$ python3 manage.py runserver

or

# use virtualenv
$ pipenv shell
(f41-erT) $ python manage.py runserver
```

## See

Then you can change extended settings without change your ```settings.py``` in path ```hellodjango/settings.d```

To be applied, files must have this pattern : ```[NAME]_settings.py```

Inside files, all settings is known from ```settings.py``` and other ```[NAME]_settings.py``` (after reading)

