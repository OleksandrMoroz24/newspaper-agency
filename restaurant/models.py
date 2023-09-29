from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Cook'
        verbose_name_plural = 'Cooks'

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return (
            f"{self.name}"
            f"{self.description}"
        )
