from django.urls import path
from django.views.generic import TemplateView

from picoplaca.platecheck.views import PlateCheckCV

app_name = "platecheck"
urlpatterns = [
    path("", PlateCheckCV.as_view(), name="check"),
    path('result/', TemplateView.as_view(template_name='platecheck/results.html'), name='result'),
]
