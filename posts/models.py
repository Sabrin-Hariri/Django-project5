# import datetime
from django.db import models
from datetime import date 

class Post(models.Model):

    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    title = models.CharField(max_length = 150)
    description = models.TextField(null=True ,blank=True)
    tags = models.CharField(max_length = 150)
    # date = models.DateField(default=date.today)

    # def __str__(self):
    #     return self.name
    