from django.db import models
from django.db.models import Model
#Create your models here.
class Contact(models.Model) :
    name  = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc  = models.TextField()
    date  = models.DateField()

    def __str__(self):
        return self.name
class Image(models.Model) :
    picture = models.BinaryField()
