from django.db import models

class Album(models.Model):
	nombre = models.CharField(max_length=140)
	artista = models.CharField(max_length=140)
	no_canciones = models.IntegerField()
	imagen = models.ImageField(upload_to = "assets", blank=True, null=True)
