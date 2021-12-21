# Rest Django Import:
from rest_framework import serializers

# Application Import:
from inventory.models.device_model import *


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


class DeviceDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceData
        fields = [
            'id',
            'device',
            'created',
            'version',
            'hostname',
            'uptime',
            'reload_reason',
            'running_image',
            'config_register',
            'hardware_list',
            'serial_list',
            'mac_list',
        ]
