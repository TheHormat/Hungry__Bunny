from django.db import models


# Create your models here.

class BurgerMenu(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Burger Menu"

    def __str__(self) -> str:
        return self.name


class DrinkMenu(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Drink Menu"

    def __str__(self) -> str:
        return self.name


class SetMenu(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Set Menu"

    def __str__(self) -> str:
        return self.name
