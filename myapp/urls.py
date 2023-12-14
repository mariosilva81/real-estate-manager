from django.urls import path
from .views import list_rentals, form_client

urlpatterns = [
    path('', list_rentals, name='list-rentals'),
    path('cadastrar/cliente', form_client, name='client-create'),
]
