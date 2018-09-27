# django-extended-settings
Apps for Django to extend global settings with additional files

Initialize other configuration settings for django project
Other configurations must be set in /path/to/project/djangoproject/settings.d/*_settings.py

        Project
        |_ apps1
        |_ ...
        |_ project
           |_ settings.py
           |_ urls.py
           |_ ...
           |_ settings.d
              |_ one_settings.py
              |_ second_settings.py
