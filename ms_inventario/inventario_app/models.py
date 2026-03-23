from django.db import models
from django.core.validators import MinValueValidator

sku = models.CharField(max_length=50, unique=True)
nombre = models.CharField(max_length=200)
descripcion = models.TextField(blank=True, null=True)
precio = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.00)])
stock = models.PositiveBigIntegerField(default=0)
foto_url = models.URLField(blank=True, null=True)

def __str__(self):
    return f"{self.sku} - {self.nombre}"
