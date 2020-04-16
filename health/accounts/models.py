from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Doctor(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=500,null=True)
    qualification = models.CharField(max_length=100,null=True)
    adhar_num = models.IntegerField(null=True)
    phone = PhoneNumberField(null=True)
    img = models.ImageField(upload_to='certifications',null=True)
    

class Pharmacist(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=500,null=True)
    qualification = models.CharField(max_length=100,null=True)
    adhar_num = models.IntegerField(null=True)
    phone = PhoneNumberField(null=True)
    img = models.ImageField(upload_to='certifications',null=True)

class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=500,null=True)
    qualification = models.CharField(max_length=100,null=True)
    adhar_no = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    phone = PhoneNumberField(null=True)
    gender = models.CharField(max_length=50,null=True)
    img = models.ImageField(upload_to='certifications',null=True)

class Prescription(models.Model):
    adhar_num = models.IntegerField(null=True)
    type = models.CharField(max_length=50,null=True)
    drug_name = models.CharField(max_length=50,null=True)
    dose = models.CharField(max_length=50,null=True)
    quantity = models.CharField(max_length=50,null=True)
    slots = models.CharField(max_length=50,null=True)
    time = models.CharField(max_length=50,null=True)
    preferred = models.CharField(max_length=50,null=True)
    note = models.CharField(max_length=150,null=True)
        
class Vitals(models.Model):
    adhar_num = models.IntegerField(null=True)
    BP = models.CharField(max_length=50,null=True)
    temperature = models.CharField(max_length=50,null=True)
    pulse_rate = models.CharField(max_length=50,null=True)
    height = models.CharField(max_length=50,null=True)
    weight = models.CharField(max_length=50,null=True)

