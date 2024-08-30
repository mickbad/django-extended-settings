# --------------------------------------------------------------------------------------------
# - Django Extended Settings
# -
# - MickBad
# --------------------------------------------------------------------------------------------

import os
import sys
import types
import glob
from django.apps import AppConfig
from django.conf import settings


# --------------------------------------------------------------------------------------------
# - Import extended settings apps
# --------------------------------------------------------------------------------------------
class ExtendedSettingsConfig(AppConfig):
    name = "extended_settings"
    verbose_name = "Extended Settings"

    def __init__(self, app_name, app_module):
        """
        Function to initialize other configuration settings for django project
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

        :return: None
        """
        # init AppConfig
        super(ExtendedSettingsConfig, self).__init__(app_name, app_module)

        # get project root path
        try:
            BASE_DIR = settings.BASE_DIR

        except AttributeError:
            raise Exception("""
** Django Extends Settings **
Please upgrade to Django 1.8+ or create on your project settings.py the following constant:

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            """)

        # get project information
        django_projectname = settings.SETTINGS_MODULE
        django_projectdir = os.path.join(BASE_DIR, django_projectname.split(".")[0])

        # read only valid settings extends files (sort files by alpha)
        list_settings_file = glob.glob(os.path.join(django_projectdir, "settings.d/*_settings.py"))
        list_settings_file.sort()
        for file_settings in list_settings_file:
            # log
            print("* Reading extends settings from {}".format(os.path.basename(file_settings)))

            # module transformation
            module_name = file_settings.split(".py")[0]
            module = types.ModuleType(module_name)
            module.__file__ = file_settings
            sys.modules[module_name] = module

            # get settings configuration for locals in sub configuration
            local_settings = {}
            instance_settings = settings.__dict__['_wrapped'].__dict__
            for k in instance_settings:
                local_settings[k] = instance_settings[k]

            # read and exec settings with current settings context
            exec(open(file_settings, "rb").read(), globals(), local_settings)

            # transform extends settings to global settings
            for var in local_settings:
                # TODO: please fix when settings.d import lib (like from mblibs.fast import FastSettings)
                try:
                    val = local_settings[var]
                    if type(val) is str:
                        exec("settings.{var}='{val}'".format(var=var, val=val.replace("'", "\\'")))
                    else:
                        exec("settings.{var}={val}".format(var=var, val=val))

                except:
                    pass


    def ready(self):
        pass

