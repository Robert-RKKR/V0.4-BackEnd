# Rest Django Import:
from rest_framework import serializers

# Application Import:
from .models import LoggerData

class LoggerDataSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'api'
        model = LoggerData
        depth = 0
        fields = '__all__'


class LoggerDataSerializerUpdateCreate(serializers.ModelSerializer):

    class Meta:
        app_label = 'api'
        model = LoggerData
        fields = '__all__'
