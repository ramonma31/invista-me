from django.db import models
from datetime import datetime

""" * Investimento
* Valor
* Pago
* Data
 """

# Create your models here.
class investimento(models.Model):
    investimento = models.TextField(max_length=20)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)