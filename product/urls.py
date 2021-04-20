from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.create_product, name='product_page'),

]
