from django.db import models

# Create your models here.

class board(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)