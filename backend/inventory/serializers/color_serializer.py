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
        fields = '__all__'


class ColorSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = '__all__'


class ColorDeviceRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorDeviceRelation
        depth = 1
        fields = '__all__'


class ColorDeviceRelationSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = ColorDeviceRelation
        fields = '__all__'


class ColorGroupRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorGroupRelation
        depth = 1
        fields = '__all__'


class ColorGroupRelationSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = ColorGroupRelation
        fields = '__all__'


class ColorCredentialRelationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ColorCredentialRelation
        depth = 1
        fields = '__all__'


class ColorCredentialRelationSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = ColorCredentialRelation
        fields = '__all__'
