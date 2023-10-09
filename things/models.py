from django.db import models


class Test(models.Model):
    quantity = models.IntegerField(max_length=100)
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30
    )
    description = models.CharField(blank=True, max_length=120)
    