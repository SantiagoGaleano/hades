from django.db import models
from datetime import datetime

# Create your models here.


class Type(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dani = models.CharField(max_length=10, unique=True, verbose_name='Número de identificacion')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    gender = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
