import csv
import io
import json

from django.db import models
try:
    from django.utils.translation import ugettext_lazy as _
except:
    from django.utils.translation import gettext_lazy as _

# ----------------------------------------------------------------------------------------------------------------------
# - Models for database settings
# ----------------------------------------------------------------------------------------------------------------------
class ExtentedSettings(models.Model):
    """
    All database application parameters
    """
    class Meta:
        db_table = "django_extended_settings"
        verbose_name = _('Parameter')
        verbose_name_plural = _(u'Parameters')
        ordering = ("name", "key", )

    # fields type
    TYPE_BOOLEAN = "boolean"
    TYPE_NUMBER = "number"
    TYPE_VARCHAR = "varchar"
    TYPE_TEXT = "text"
    TYPE_CHOICES = (
        (TYPE_BOOLEAN, _("Yes/No")),
        (TYPE_NUMBER, _("Number")),
        (TYPE_VARCHAR, _("Text field")),
        (TYPE_TEXT, _("Multiline text field")),
    )

    # primary fields
    name = models.CharField(max_length=1024, verbose_name=_("Configuration"), help_text=_("Configuration name"))
    key = models.CharField(max_length=255, verbose_name=_("Parameter name"))
    value = models.TextField(blank=True, null=True, verbose_name=_("Value"))
    # type = models.CharField(max_length=50,
    #                         choices=TYPE_CHOICES,
    #                         default=TYPE_VARCHAR,
    #                         help_text=_("Field type"),
    #                         verbose_name=_("Type"))

    # model management
    enabled = models.BooleanField(default=True, verbose_name=_("Activation"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated_at"))

    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return self.name

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set(key: str, value, name: str = ""):
        """
        Set new value in key
        """
        try:
            o = ExtentedSettings.objects.get(key=key)

        except:
            # not found, create it
            o = ExtentedSettings()
            o.name = f"Option {key}" if name is None or len(name.strip()) < 1 else name
            o.key = key
            pass

        # set value
        o.value = value
        o.save()

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def set_data(key: str, value, name: str = ""):
        """
        Stocke une liste (ou toute structure JSON) sous forme de chaîne (non JSON : on retire les [] ou {} entourant la phrase).
 
        :param key: clé de configuration
        :param values: liste/dictionnaire à enregistrer
        :return: None
        """
        if not isinstance(value, (list, dict)):
            raise ValueError("values must be a list")

        # Convert JSON
        formatted_value = json.dumps(value)
        formatted_value = formatted_value[1:-1]

        # save
        ExtentedSettings.set(
            key=key,
            value=formatted_value,
            name=name,
        )
    
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get(key: str, default=""):
        """
        get configuration value

        :param key: configuration key
        :param default: default value if error
        :return: String
        """
        try:
            o = ExtentedSettings.objects.get(key=key)
            return str(o.value)

        except:
            # not found!
            return default

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_boolean(key: str, default=False):
        """
        get configuration value (boolean)

        :param key: configuration key
        :param default: default value if error
        :return: String
        """
        try:
            value = ExtentedSettings.get(key, "no")
            if value.lower().strip() in ("yes", "oui", "true", "1", "si", "ja", "y", "o", "t", "s", "j"):
                return True
            return False

        except:
            # pas trouvé!
            return default

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_int(key: str, default=0):
        """
        get configuration value (int)

        :param key: configuration key
        :param default: default value if error
        :return: String
        """
        try:
            return int(ExtentedSettings.get(key, default))

        except:
            # pas trouvé!
            return default

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_float(key: str, default=0.0):
        """
        get configuration value (float)

        :param key: configuration key
        :param default: default value if error
        :return: String
        """
        try:
            value = ExtentedSettings.get(key, default).replace(",", ".")
            return float(value)

        except:
            # pas trouvé!
            return default

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_data(key, default=None, delimiter: str =",", quotechar: str ="\""):
        """
        Récupère une liste ou structure JSON stockée sous forme de chaîne.

        :param key: clé de configuration
        :param default: valeur par défaut si la clé est absente
        :param delimiter: séparateur entre les éléments de la liste
        :param quotechar: caractère entourant les valeurs (ex: guillemets)
        :return: Liste/Dictionnaire
        """
        value = ExtentedSettings.get(key, None)
        if value is None:
            return default 

        # JSON content?
        try:
            # try list
            return json.loads(f"[{value}]")
        except json.JSONDecodeError:
            # not json : try dict
            try:
                return json.loads("{" + value + "}")
            except json.JSONDecodeError:
                # not json
                pass 

        # Fallback : CSV parse
        reader = csv.reader(io.StringIO(value), delimiter=delimiter, quotechar=quotechar)
        parsed_list = next(reader, default)

        # convert int (ex: "2" -> 2)
        def convert_type(x):
            """
            Try to convert value to str, int, float, bool
            """
            x = str(x).strip()

            # Convert to bool
            x_lower = x.lower()
            if x_lower in ("true", "false"):
                return x_lower == "true"

            # Convert to int
            if x.lstrip("-").isdigit():
                return int(x)

            # Convert float
            if x.lstrip("-").replace('.', '', 1).isdigit():
                return float(x)

            # else original x value (stripped)
            return x

        return [convert_type(x) for x in parsed_list]

    # ------------------------------------------------------------------------------------------------------------------
    def custom_field_value(self, cut=50):
        """
        Display parameter value strip
        :param cut: strip number
        :return: str
        """
        value = str(self.value).replace('\n', ' ').replace('\r', '')
        return value if len(value) < cut else value[0:cut] + "..."
    custom_field_value.short_description = _("Value")
