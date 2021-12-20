# Rest Django Import:
from rest_framework import serializers

# Application Import:
from inventory.models.color_model import Color


class ColorModifySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = [
            'active',
            'name',
            'hexadecimal',
            'description',
            'devices',
            'groups',
            'credentials',
        ]


class ColorGetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = [
            'id',
            'created',
            'updated',
            'active',
            'name',
            'hexadecimal',
            'description',
            'devices',
            'groups',
            'credentials',
        ]
