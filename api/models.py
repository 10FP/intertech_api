from django.db import models

# Create your models here.

class Createuser(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    face = models.ImageField()
    id_number = models.IntegerField()
    birth_date = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    document_no = models.CharField(max_length=10)
    until_valid = models.CharField(max_length=10)
    nation = models.CharField(max_length=50)
    qr_code = models.ImageField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)

    def __str__(self):
        return f"name: {self.name}, surname: {self.surname}, id_number: {self.id_number}"