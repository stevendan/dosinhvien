from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=30)
    password = models.TextField()
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    sex = models.BooleanField(default=0)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook = models.CharField(max_length=100)
    last_login = models.DateTimeField()

class Product(models.Model):
    name = models.TextField()
    user_id = models.IntegerField()
    category_id = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    price = models.IntegerField()
    time_of_post = models.DateTimeField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
