from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import admin
from django.conf import settings
from django.db import models


class MyModel(models.Model):
    pass


#your abstracting data from the django documentation and manipulating it
class User(AbstractUser):
    pass
    

    def __str__(self):
       return self.username


