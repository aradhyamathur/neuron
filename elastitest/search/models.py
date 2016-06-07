from __future__ import unicode_literals

from django.db import models
import django.db.models.options as options

options.DEFAULT_NAMES = options.DEFAULT_NAMES \
                        + ('es_index_name', 'es_type_name', 'es_mapping')
# Create your models here.


class PersonDb(models.Model):

    name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        es_index_name = 'django_person'
        es_type_name = 'person'
        es_mapping = {
            'properties': {
                'name': {'type': 'string', 'index': 'not_analyzed'},
                'address': {'type': 'string', 'index': 'not_analyzed'},
                'age': {'type': 'short'},
            }
        }
