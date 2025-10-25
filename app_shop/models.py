from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # description = models.TextField(null=True, blank=True)
    description = CKEditor5Field(config_name='extends',null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/products')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=200)
#     avatar = models.ImageField(upload_to='images/avatars/',default='images/avatars/noavatar.png')

#     def __str__(self):
#         return self.name