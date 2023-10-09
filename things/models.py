from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

class Test(models.Model):
    quantity = models.IntegerField(
        validators=[MinLengthValidator(0), MaxValueValidator(100)]
    )
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(blank=True, max_length=120)
    