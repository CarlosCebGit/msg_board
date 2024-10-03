from django.db import models

# Create your models (tablas de la base de datos)
class publication(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:50]
