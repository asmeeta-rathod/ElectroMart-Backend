from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.

s3_storage = S3Boto3Storage()

class Category(models.Model):
    name= models.CharField(max_length=100);

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(storage=s3_storage, upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
