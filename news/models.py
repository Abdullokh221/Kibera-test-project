from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=100)
    date_uploaded = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title