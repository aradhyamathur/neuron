import elasticpy as ep
import pytest
from django.test import TestCase


class TestConn(TestCase):

    def test_query(self):
        query = ep.ElasticQuery().query_string(query='anm')
        search = ep.ElasticSearch()
        self.assertTrue(search.search_advanced('student', 'info', query))
