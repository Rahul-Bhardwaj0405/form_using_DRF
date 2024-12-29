from django.db import models

# Create your models here.

class FormData(models.Model):
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    address = models.TextField()
    dob = models.DateField()
    phone_number = models.IntegerField()
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name


    