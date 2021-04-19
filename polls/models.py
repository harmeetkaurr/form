from django.db import models

# Create your models here.
class college_form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=50)
    course = models.CharField(max_length=50,
                              choices=[
        ('bca', 'BCA'),
        ('bba', 'BBA'),
        ('b.tech', 'B.Tech'),
        ('mca', 'MCA'),
        ('m.sc', 'M.Sc'),
        ('m.tech', 'M.Tech'),
    ])
    
    
class student_form(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    classes = models.CharField(max_length=50,
                               choices=[
        ('1', 'I'),
        ('2', 'II'),
        ('3', 'III'),
        ('4', 'IV'),
        ('5', 'V'),
        ('6', 'VI'),
        ('7', 'VII'),
        ('8', 'VIII'),
        ('9', 'IX'),
        ('10', 'X'),
        ('11', 'XI'),
        ('12', 'XII'),
    ])
    
    
class login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    retype_password = models.CharField(max_length=50)

