from uuid import uuid4
from django.db import models


class Client(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(max_length=200, verbose_name="E-mail")
    phone = models.CharField(max_length=15, verbose_name="Telefone")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.name, self.email, self.phone)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class RealEstateTypes(models.TextChoices):
    APARTMENT = "Apartamento", "Apartamento"
    KITNET = "Kitnet", "Kitnet"
    HOUSE = "Casa", "Casa"


class RealEstate(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=100, blank=True, verbose_name="Cód.")
    type = models.CharField(
        max_length=100, choices=RealEstateTypes.choices, verbose_name="Tipo"
    )
    address = models.TextField(verbose_name="Endereço")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    is_rented = models.BooleanField(default=False, verbose_name="Alugado?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.code, self.type, self.id)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_default_code()
        super().save(*args, **kwargs)

    def generate_default_code(self):
        type_prefix = self.type[:3].upper()
        sequential_number = RealEstate.objects.count() + 1
        return f"{type_prefix}{sequential_number:03d}"


class RealEstateImage(models.Model):
    image = models.ImageField("Images", upload_to="images")
    real_estate = models.ForeignKey(
        RealEstate, related_name="real_estate_images", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.real_estate.code


class RentalRegister(models.Model):
    real_estate = models.ForeignKey(
        RealEstate, related_name="rental_register", on_delete=models.CASCADE
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateTimeField("Início")
    end_date = models.DateTimeField("Fim")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} - {}".format(self.client, self.real_estate)

    class Meta:
        verbose_name = "Registrar Locação"
        verbose_name_plural = "Registrar Locação"
