from django.db import models
from uuid import uuid4
from  os import path

# Create your models here.
class Category(models.Model):


    def get_file_name(self,filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('media/images/categories', filename)

    title = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}:{self.category_order}'

class Dish(models.Model):
    def get_file_name(self,filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('media/images/dishes', filename)

    title = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}:{self.price}'

class History(models.Model):
    def get_file_name(self,filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('media/images/history', filename)

    title = models.CharField(max_length=25, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    desc = models.CharField(max_length=150, unique=True)


    def __str__(self):
        return f'{self.title}'


class Chef(models.Model):
    def get_file_name(self,filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('media/images/chef', filename)

    title = models.CharField(max_length=15, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    desc = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f'{self.title}'

class Phone(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.phone}'

class Adress(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=10)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.city}; {self.street}; {self.building}'

class OpeningHours(models.Model):
    day = models.CharField(max_length=12)
    hours_start = models.CharField(max_length=8)
    hours_end = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.day} - {self.hours_start} - {self.hours_end}'

class CafeInfo(models.Model):
    adress_id = models.ForeignKey(Adress, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    is_visible = models.BooleanField(default=True)

class Message(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=400)
    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name} : {self.user_email} : {self.user_message[:20]}'