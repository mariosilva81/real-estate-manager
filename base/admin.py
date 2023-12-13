from django.contrib import admin

from myapp.models import Client, RealEstate

# Register your models here.
admin.site.register(Client)
admin.site.register(RealEstate)
