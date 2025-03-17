# django-extended-settings
Apps for Django to extend global settings with additional files

Initialize other configuration settings for django project
Other configurations must be set in /path/to/project/djangoproject/settings.d/*_settings.py

        Project/
        |_ apps1/
        |_ ...
        |_ project/
           |_ settings.py
           |_ urls.py
           |_ ...
           |_ settings.d/
              |_ one_settings.py
              |_ second_settings.py

The current version of the Django Extended Settings is 1.3.1. It works on Django ≥ 5.0.

### Installation

#### Getting the code

The recommended way to install the Django Extended Settings is via pip or pipenv:

```bash
$ pip install django-extended-settings
```

#### Prerequisites

Make sure add ```extended_settings``` to your ```INSTALLED_APPS``` setting:

```python
INSTALLED_APPS = [
    # ...
    'extended_settings',
    # ...
]
```

#### Play settings into your project

Create sub directory ```settings.d/``` into django project directory and put your configuration into independant files with this patterns ```*_settings.py```

__sample__  : ```/path/to/project/djangopython/settings.d/production_settings.py```


#### Play database settings

You can add some settings in database

```$ ./manage.py migrate ```

In your python files, you can create settings (in command for example) like this

```python
from extended_settings.models import ExtentedSettings

o = ExtentedSettings()
o.name = "My home page location"
o.key = "hostname"
o.value = "http://localhost:8000"
o.save()
```

better alternative,

```python
from extended_settings.models import ExtentedSettings

ExtentedSettings.set(
    key="hostname",
    value="http://localhost:8000",
    name="My home page location",
)

ExtentedSettings.set_data(
    key="data",
    value=["Aron Run", "toto marche", "mistal:online", -3.14, True, False, {"val": 2}],
    name="My list",
)
```

To retrieve settings in your views, ...

```python
from extended_settings.models import ExtentedSettings

my_var = ExtentedSettings.get("hostname")
my_var = ExtentedSettings.get("hostname", 'default value')

my_int = ExtentedSettings.get_int("my-int")
my_float = ExtentedSettings.get_float("my-float", 100.0)
my_bool = ExtentedSettings.get_boolean("my-bool") # True = yes, y, true, 1, ...

my_list = ExtentedSettings.get_data("data")
>>> ['Aron marcel', 'toto marche', 'mistral:online', -3.14, True, False, {"val": 2}]
```


### Misc

The Django Extended Settings is released under the BSD license, like Django itself. If you like it, please consider contributing!

The Django Extended Settings was originally created by Mickael Badet in September 2018.

*Special thanks to contributer JunkyDeveloper for Django ≥ 5.0, Python 3.12 fix.*

