from rest_framework import serializers
from .models import PersonDb


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonDb
        fields = '__all__'
