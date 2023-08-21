from django.db import models

# Create your models here.

class IdCardPhoto(models.Model):
    id_card_front = models.CharField(max_length=100000)
    id_card_back = models.CharField(max_length=100000)

