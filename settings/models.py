from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/')
    subtitle = models.CharField(max_length=500)
    fb_link = models.URLField(null=True , blank=True)
    tw_link = models.URLField(null=True , blank=True)
    ins_link = models.URLField(null=True , blank=True)
    address = models.TextField(max_length=200)
    phone_number = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    call_us = models.CharField(max_length=25)
    email_us = models.EmailField()

    def __str__(self):
        return self.name
    

