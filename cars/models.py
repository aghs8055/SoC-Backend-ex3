from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from model_utils.models import UUIDModel
from django.db.models import CheckConstraint, Q


class BrandTypeChoices(models.TextChoices):
    Benz = ("Benz", "Benz")
    BMW = ("BMW", "BMW")
    Porche = ("Porche", "Porche")


class Car(UUIDModel):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, choices=BrandTypeChoices.choices)
    year_built = models.DateField()
    mileage = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(price__gt=0),
                name="price_must_be_greater_than_zero"
            ),
        ]

    def get_price(self, brand, year_built):
        # TODO: Complete here using cache
        # FIXME: use `from functools import cache`
        pass
