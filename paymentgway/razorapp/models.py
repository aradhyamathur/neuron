from __future__ import unicode_literals

from django.db import models
from django.core.validators import EmailValidator


class Payee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[EmailValidator])
    cid = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=250, blank=False, default=None)

    def __str__(self):
        return self.name


# class Purchase(models.Model):
#     cid = models.ForeignKey(Payee)
#     pay_id = models.CharField(max_length=200, primary_key=True)
#
#     def __str__(self):
#         return self.pay_id
#
#
# class PurchaseDetails(models.Model):
#     pid = models.ForeignKey(Purchase, on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.product_name
