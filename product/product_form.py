from django.forms import models

import product
from product.models import Product


class Product_form(models.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'