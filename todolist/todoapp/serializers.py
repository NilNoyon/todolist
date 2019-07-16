from rest_framework import serializers
from rest_framework_bulk.drf3.serializers import BulkSerializerMixin, BulkListSerializer
from todoapp.models import *

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = '__all__'