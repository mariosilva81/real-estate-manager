from django.urls import path
from .views import form_real_estate, list_real_estates, form_client, form_rental

urlpatterns = [
    path("", list_real_estates, name="list-real-estates"),
    path("cadastrar/cliente", form_client, name="client-create"),
    path("cadastrar/imovel", form_real_estate, name="real-estate-create"),
    path("locacao/<uuid:real_estate_id>", form_rental, name="rental-create"),
]
