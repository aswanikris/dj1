from django.db import models

# Create your models here.
class tab(models.Model):
    title=models.CharField(max_length=256)
    def __str__(self):
        return self.title

