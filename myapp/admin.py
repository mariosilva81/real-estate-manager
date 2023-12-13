from django.contrib import admin
from myapp.models import Client, RealEstate, RealEstateImage, RentalRegister


admin.site.register(Client)
admin.site.register(RentalRegister)


class RealEstateImageInlineAdmin(admin.TabularInline):
    model = RealEstateImage
    extra = 0


class RealEstateAdmin(admin.ModelAdmin):
    inlines = [RealEstateImageInlineAdmin]


admin.site.register(RealEstate, RealEstateAdmin)
