from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel
from ckeditor.fields import RichTextField


# Create your models here.

class Product(TimeStampedModel):
    title = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
