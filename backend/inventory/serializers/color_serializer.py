# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.color_model import Color


class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        depth = 1
        fields = [
            'id',
            'created',
            'updated',
            'root',
            'active',
            'name',
            'hexadecimal',
            'description',
            'devices',
            'groups',
            'credentials',
        ]
