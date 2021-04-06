from django.contrib import admin
from picoplaca.platecheck.models import PlateCheck
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)  # Protect admin from being bruteforeced


@admin.register(PlateCheck)
class MiaMCAdmin(SimpleHistoryAdmin):
    list_display = ("platecheck_plate", "platecheck_date", "platecheck_time",)
