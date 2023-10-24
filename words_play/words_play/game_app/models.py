#Game
from django.db import models
from django.conf import settings
import random

# Create your models here.
class Word(models.Model):
    word = models.TextField()
    description = models.TextField() 

    def __str__(self):
        return self.word
