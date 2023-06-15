from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    desc=serializers.CharField()
    price=serializers.IntegerField()
    offer=serializers.BooleanField(default=False)
