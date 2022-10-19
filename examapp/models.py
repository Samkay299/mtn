from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=15)
    web = models.URLField(blank=True)
    Email_address = models.EmailField(blank=True)
    Male = "Male"
    Female = 'Female'
    choices = ((Male, "Male"), (Female, "Female"))
    gender = models.CharField('Gender', max_length=6, choices=choices)


    def __str__(self):
        return self.name