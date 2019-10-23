from django.db import models


class Persona(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido= models.CharField(max_length=50)
    NumEmpleado = models.CharField(max_length=10)


class Empleado(models.Model):
    CATEGORIAS = (
        ('0', 'Estudiante'),
        ('1', 'Maestro'),
        ('2', 'Administrativo')
    )
    categoria = models.CharField(choices=CATEGORIAS, max_length=2) 
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='individuos', related_query_name='individuo')