from django.db import models

# Create your models here.
class Roll(models.Model):
        immagine = models.ImageField()
        nome =models.CharField(max_length=20)
        descrizione = models.CharField(max_length=50)
        prezzo = models.FloatField()

        def __str__(self) -> str:
                return self.nome