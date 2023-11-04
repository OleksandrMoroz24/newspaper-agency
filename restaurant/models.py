from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    photo = models.ImageField(upload_to="photos/cooks", default="photos/cooks/default.jpg")
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        related_name="dishes",
        on_delete=models.CASCADE
    )
    cooks = models.ManyToManyField(Cook, related_name="dishes")
    photo = models.ImageField(upload_to="photos/dishes", default="photos/dishes/default.jpg")

    def __str__(self):
        return (
            f"{self.name}"
            f"{self.description}"
        )

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
