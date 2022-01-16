# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.color_model import Color

# API Variable Import:
from api.variables import DEFAULT_DEPTH


class ColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        depth = DEFAULT_DEPTH
        fields = '__all__'


class ColorSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Color
        fields = '__all__'
