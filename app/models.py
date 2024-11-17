from django.db import models

# Create your models here.


class reserva(models.Model):
    rg_cliente = models.CharField(max_length=255, null=True)
    nome_cliente = models.CharField(max_length=255, null=True)
    email_cliente = models.EmailField(null=True)
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    hora_inicio = models.TimeField(null=True)
    hora_fim = models.TimeField(null=True)
    tipo_reserva = models.CharField(max_length=20, null=True)
    pagto = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.rg_cliente
    
