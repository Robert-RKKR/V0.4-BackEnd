# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.color_model import ColorCredentialRelation
from ..models.color_model import ColorDeviceRelation
from ..models.color_model import ColorGroupRelation
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


class ColorDeviceRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorDeviceRelation
        depth = 1
        fields = [
            'id',
            'created',
            'updated',
            'root',
            'device',
            'color',
        ]


class ColorGroupRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorGroupRelation
        depth = 1
        fields = [
            'id',
            'created',
            'updated',
            'root',
            'group',
            'color',
        ]


class ColorCredentialRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorCredentialRelation
        depth = 1
        fields = [
            'id',
            'created',
            'updated',
            'root',
            'credential',
            'color',
        ]
