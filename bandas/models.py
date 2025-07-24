from django.db import models

class Genero(models.Model):
  nombre = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return self.nombre

class Banda(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
  portada = models.URLField(blank=True, null=True, help_text="URL completa de la imagen (ej. https://placehold.co/300x300)")

  def __str__(self):
    return self.nombre