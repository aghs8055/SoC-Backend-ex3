from functools import cache

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

    @cache
    def get_price(self, brand, year_built):
        return len(brand) * year_built * 100
    
    def get_price_cache_info(self):
        return self.get_price.cache_info()
