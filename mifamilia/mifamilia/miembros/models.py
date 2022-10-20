from datetime import datetime
from django.db import models
from unittest.util import _MAX_LENGTH
from datetime import datetime

# Create your models here.

class Miembro(models.Model):

     nombre = models.CharField(max_length=50)
     fecha_nac = models.DateField()
     edad = models.IntegerField()