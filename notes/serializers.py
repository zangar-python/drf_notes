from rest_framework import serializers
from .models import node

class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = node
        fields = '__all__'