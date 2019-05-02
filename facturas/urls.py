from django.urls import path
from facturas import views

app_name = 'facturas'

urlpatterns = [
    path(route='', view=views.home, name='home'),
]

