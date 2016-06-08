from django.core.management.base import BaseCommand
from elastitest.base_client import ES_CLIENT
from elasticsearch.client import IndicesClient
from search.models import PersonDb
from elasticsearch.helpers import bulk


class Command(BaseCommand):

    help = "Push to index"

    def handle(self, *args, **options):
        pass


class Command(BaseCommand):
    help = "Push to index"

    def handle(self, *args, **options):
        self.recreate_index()

    def recreate_index(self):
        indices_client = IndicesClient(client=ES_CLIENT)
        index_name = PersonDb._meta.es_index_name
        if indices_client.exists(index_name):
            indices_client.delete(index=index_name)
        indices_client.create(index=index_name)
        indices_client.put_mapping(
            doc_type=PersonDb._meta.es_type_name,
            body=PersonDb._meta.es_mapping,
            index=index_name
        )

    def push_db_to_index(self):
        data = [self.convert_for_bulk(s, 'create') for s in PersonDb]
        print "data to be pushed \n", data
        bulk(client=ES_CLIENT, actions=data, stats_only=True)

    def convert_for_bulk(self, django_object, action=None):
        data = django_object.es_repr()
        metadata = {
            '_op_type': action,
            '_index': django_object._meta.es_index_name,
            '_type': django_object._meta.es_type_name,
        }
        data.update(**metadata)
        print "data for bulk \n", data
        return data

    def field_es_repr(self, field_name):
                    config = self._meta.es_mapping['properties'][field_name]
                    if hasattr(self, 'get_es_%s' % field_name):
                        field_es_value = getattr(self, 'get_es_%s' % field_name)()
                    else:
                        if config['type'] == 'object':
                            related_object = getattr(self, field_name)
                            field_es_value = {}
                            field_es_value['_id'] = related_object.pk
                            for prop in config['properties'].keys():
                                field_es_value[prop] = getattr(related_object, prop)

                        else:
                            field_es_value = getattr(self, field_name)

                    return field_es_value

    def es_repr(self):
        data = {}
        mapping = self._meta.es_mapping
        data['_id'] = self.pk

        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)

        return data

    def get_es_person_complete(self):
        return {"input": [self.name, self.address, self.age],
                "output": "%s %ss" % (self.name, self.address),
                "payload ": {"pk": self.pk}
                }





