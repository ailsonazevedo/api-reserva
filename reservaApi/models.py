from django.db import models
import uuid
from django.db.models.fields import DateTimeField



class Key (models.Model):
    nome = models.CharField('Nome da chave',max_length=150)
    numero = models.DecimalField('Número da chave', max_digits=5,decimal_places=0,null=False, blank=False)

    def __str__(self):
        return str(self.numero)

    class Meta:
        ordering = ['numero']
        verbose_name = 'Chave'
        verbose_name_plural = 'Chaves'

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    reservation = models.BooleanField('Reservado?',default=True)
    first_name = models.CharField('Primeiro Nome',max_length=100)
    last_name = models.CharField('Ultimo Nome',max_length=100)
    date_reservation = DateTimeField('Data da Reserva',auto_now_add=True,null=False)
    date_devolution = DateTimeField('Data da Devolução',auto_now=False,null=True, blank=True)
    key = models.ForeignKey(Key,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['date_reservation']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

# Create your models here.
