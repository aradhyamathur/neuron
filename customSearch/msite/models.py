from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    rno = models.IntegerField()
    address = models.CharField(max_length=50)
    rno = models.IntegerField(primary_key=True)
    analysis = models.TextField()

    def __str__(self):
        return self.name
