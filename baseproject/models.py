from django.db import models

# Create your models here.

class Developer(models.Model):
    username = models.CharField(max_length=225)
    bio = models.CharField(max_length=500, null=True, blank=True)
    # sex
    # photo

    def __str__(self):
        return self.username