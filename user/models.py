from django.db import models
from django.core.validators import *


class User(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    store_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    user_image = models.ImageField(upload_to="templates/media")

    def __str__(self):
        return self.name
