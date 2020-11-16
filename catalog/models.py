from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """Category class """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product class"""

    name = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, related_name="product")
    # nutrition_image = models.URLField(null=True)
    # description = models.CharField(max_length=1000, null=False)
    nutrition_grade = models.CharField(max_length=1, null=False)
    image = models.URLField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=False)
    calories = models.CharField(max_length=5, null=True)
    lipids = models.CharField(max_length=5, null=True)
    sugars = models.CharField(max_length=5, null=True)
    proteins = models.CharField(max_length=5, null=True)
    salts = models.CharField(max_length=5, null=True)
    url = models.URLField(null=False)

    def __str__(self):
        return self.name


class UserFavorite(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
