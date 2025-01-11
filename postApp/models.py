from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)
    
