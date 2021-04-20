from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.core.validators import *

from user.models import User

CATEGORIES_CHOICE = (
    ("Categories", "Category"),
    ("kiddies", "kids"),
    ("Technologies", "Tech"),
    ("MEN", "MEN")
)


class Product(models.Model):
    marchant = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="templates/media")
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    categories = models.CharField(max_length=50, choices=CATEGORIES_CHOICE, default="Categories")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.name
