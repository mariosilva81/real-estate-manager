from uuid import uuid4
from django.db import models


class Client(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} - {} - {}'.format(self.name, self.email, self.phone)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class RealEstateTypes(models.TextChoices):
    APARTMENT = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'CASA', 'CASA'


class RealEstate(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=RealEstateTypes.choices)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_rented = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{} - {}'.format(self.code, self.type)

    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'


class RealEstateImage(models.Model):
    image = models.ImageField('Images', upload_to='images')
    real_estate = models.ForeignKey(RealEstate, related_name='real_estates_images', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.real_estate.code
