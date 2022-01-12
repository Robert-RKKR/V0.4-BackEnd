# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.device_model import *


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        depth = 1
        fields = '__all__'


class DeviceSerializerUpdateCreate(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class DeviceDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceData
        depth = 1
        fields = '__all__'


class DeviceDataSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceData
        fields = '__all__'
