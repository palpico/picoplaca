from django.urls import path
from django.views.generic import TemplateView


app_name = "platecheck"
urlpatterns = [
    path('result/', TemplateView.as_view(template_name='platecheck/results.html'), name='result'),
]
