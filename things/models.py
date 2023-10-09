from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    