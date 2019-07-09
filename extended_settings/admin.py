from django.contrib import admin
from extended_settings.models import ExtentedSettings

# ----------------------------------------------------------------------------------------------------------------------
# - Création de l'administration des paramètres
# ----------------------------------------------------------------------------------------------------------------------
@admin.register(ExtentedSettings)
class ExtentedSettingsAdmin(admin.ModelAdmin):
    """
    Parameters Administration
    """
    readonly_fields = ("name", "key", "updated_at")
    list_display = ("name", "custom_field_value", "updated_at")

    fieldsets = (
        (None, {
            "fields": ("name",
                       "key",
                       "value",
                       "updated_at",)
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

