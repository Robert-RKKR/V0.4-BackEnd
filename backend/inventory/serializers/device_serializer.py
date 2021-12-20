# Rest Django Import:
from rest_framework import serializers

# Application Import:
from inventory.models.device_model import Device


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = [
            'id',
            'created',
            'updated',
            'active',
            'ssh_status',
            'https_status',
            'name',
            'hostname',
            'device_type',
            'ico',
            'ssh_port',
            'https_port',
            'description',
            'credential',
            'secret',
            'token',
            'certificate',
        ]
