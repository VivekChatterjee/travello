from django.db import models

# Create your models here.

# class Destination:
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int
#     offer: bool

class Destination(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField() 
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()


class Product(models.Model):
    pass