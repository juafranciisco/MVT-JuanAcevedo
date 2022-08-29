from django.urls import path
from Familiares.views import probar_template


urlpatterns = [
    path('', probar_template),
]