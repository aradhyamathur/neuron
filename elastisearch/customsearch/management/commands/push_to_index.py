from django.core.management.base import BaseCommand
from django.conf import settings
from conf import base
from customsearch.models import University, Course, Students
from django.core.management.base import  BaseCommand
from elasticsearch.client import IndicesClient



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.recreate_index()

    def recreate_index(self):
        indices_client = IndicesClient(client=base.ES_CLIENT)
        index_name = Students._meta.es_index_name

        if indices_client.exists(index=index_name):
            indices_client.delete(index=index_name)

        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=Students._meta.es_type_name,
            body=Students._meta.es_mapping,
                index=index_name
            )
