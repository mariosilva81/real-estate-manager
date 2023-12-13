from django.urls import path
from .views import list_rentals

urlpatterns = [
    path('', list_rentals, name='list-rentals'),
]
