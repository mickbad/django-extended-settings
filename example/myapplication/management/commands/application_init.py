"""
Scripts de lancement de commande pour ajouter des données à l'application courante

cf: https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html
"""
# libs
from django.conf import settings as django_settings
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from extended_settings.models import ExtentedSettings


class Command(BaseCommand):
    help = 'Seed default settings in application'

    def handle(self, *args, **kwargs):
        """
        Populate some rows into database
        """
        # --------------------------------------------------------------------------------------------------------------
        # Création des paramètres par défaut
        my_settings = (
            ("Website address", "hostname", "http://localhost:8000", ExtentedSettings.TYPE_VARCHAR),
            ("Titre", "title", django_settings.PROJECT_NAME, ExtentedSettings.TYPE_VARCHAR),
        )
        for conf in my_settings:
            try:
                ExtentedSettings.objects.get(key=conf[1])
                self.stdout.write(self.style.WARNING("configuration \"{}\" already exists.".format(conf[1])))

            except:
                try:
                    o = ExtentedSettings()
                    o.name = conf[0]
                    o.key = conf[1]
                    o.value = conf[2]
                    # o.type = conf[3]
                    o.save()
                    self.stdout.write(self.style.SUCCESS("configuration \"{}\" is created.".format(conf[1])))

                except Exception as e:
                    self.stdout.write(self.style.ERROR("configuration \"{}\" failed: {}.".format(conf[1], str(e))))
