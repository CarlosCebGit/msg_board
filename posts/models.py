from django.db import models

# Create your models (tablas de la base de datos)
class Publication(models.Model):
    text = models.TextField()
