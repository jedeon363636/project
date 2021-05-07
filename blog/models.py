from django.db import models
from django.db.models.fields import DateField

class TimespamtesModel(models.Model):
    create_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True


#Create your models here.

class Post(TimespamtesModel):
    title = models.CharField(max_length=250)
    body = models.TextField()
   


    def __str__(self):
        return self.title




