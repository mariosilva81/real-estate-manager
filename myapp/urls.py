from django.urls import path
from .views import mysite

urlpatterns = [
    path('', mysite, name='mysite'),
]
