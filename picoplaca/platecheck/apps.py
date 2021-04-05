from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlatecheckConfig(AppConfig):
    name = 'picoplaca.platecheck'
    verbose_name = _("Plate Check")
