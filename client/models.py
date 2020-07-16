from django.db import models

from datetime import datetime
# Create your models here.

from django.contrib.auth.models import User

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        
        
 
class Category(TimeStampMixin):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}'
    

class Food(TimeStampMixin):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='foodsimage')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField()
    
    def __str__(self):
        return f'{self.name} => {self.category.name} {self.updated_at}'
  

class Reason(TimeStampMixin):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}'
      
class Event(TimeStampMixin):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='eventsimage')
    
    def __str__(self):
        return f'{self.name}'
     
class Info(models.Model):
    location        = models.CharField(max_length=100)
    dateOuvertes    = models.CharField(max_length=100)
    heureOuvertes   = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    phoneNumber     = models.CharField(max_length=20)
    googleMapsLink  = models.TextField()
    
    def __str__(self):
        return f'Les infos '    
     

#user = models.ForeignKey(User, related_name='following')

class Reservation(TimeStampMixin):
    name        = models.CharField(max_length=100)
    email       = models.EmailField(max_length=254)
    phoneNumber = models.CharField(max_length=20)
    date        = models.DateField()
    time        = models.TimeField()
    nbOfPeople  = models.IntegerField()
    message     = models.TextField()
       
    def __str__(self):
        return f'{self.name} pour {self.date} à {self.time} et {self.nbOfPeople} pers'