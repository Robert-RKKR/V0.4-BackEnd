# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.device_model import *


class DeviceSerializerAll(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = '__all__'


class DeviceSerializerLimited(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'active',
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
