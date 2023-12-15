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

admin.site.site_header = 'Real Estate Manager'
admin.site.site_title = 'Real Estate Manager'
admin.site.index_title = 'Painel de Administração do Real Estate Manager'
