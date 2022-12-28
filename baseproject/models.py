from django.db import models

# Create your models here.

class Developer(models.Model):
    username = models.CharField(max_length=225)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
    male = 'male'
    female = 'female'
    other = 'other'
    sex_choices = [(male, 'male'), (female, 'female'),(other, 'other')]
    sex =models.CharField(max_length=10, choices=sex_choices, default=other)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username
    

class Company(models.Model):
    companyname=models.CharField(max_length=250)
    bio=models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.companyname