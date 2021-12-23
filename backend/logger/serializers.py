# Rest Django Import:
from rest_framework import serializers

# Application Import:
from .models import LoggerData

class LoggerDataSerializer(serializers.ModelSerializer):

    class Meta:
        app_label = 'api'
        model = LoggerData
        depth = 1
        fields = [
            'id',
            'timestamp',
            'severity',
            'message',
            'connection',
            'device',
            'color',
            'credential',
            'group',
        ]
