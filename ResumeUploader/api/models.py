from django.db import models


# Create your models here.
State_Choice = ((
    ('Bihar', 'Bihar'),
    ('West Bengal', 'West Bengal'),
    ('Gujarat', 'Gujarat'),
    ('Maharashtra', 'Maharashtra'),
    ('Goa', 'Goa'),
    ('Delhi','Delhi'),
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=State_Choice, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimg = models.ImageField(upload_to='pimages', blank=True)
    docs = models.FileField(upload_to='documents', blank=True)
