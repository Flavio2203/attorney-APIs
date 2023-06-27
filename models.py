from django.db import models

# Create your models here.

class Processo(models.Model):
    periodotempo = models.DateField(max_length=100)
    contagemencadeamento = models.IntegerField(max_length=12)
    tipoprocesso = models.CharField(max_length=100)


