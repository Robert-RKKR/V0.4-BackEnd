# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.device_model import Device
from ..models.device_model import DeviceData
from ..models.device_model import DeviceRawData
from ..models.device_model import DeviceInterface


# Device Serializer:
class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        depth = 1
        fields = '__all__'


class DeviceSerializerUpdateCreate(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


# Device Data Serializer:
class DeviceDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceData
        depth = 1
        fields = '__all__'


class DeviceDataSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceData
        fields = '__all__'


# Device Device RawData Serializer:
class DeviceRawDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceRawData
        depth = 1
        fields = '__all__'


class DeviceRawDataSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceRawData
        fields = '__all__'


# Device Data Serializer:
class DeviceInterfaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceInterface
        depth = 1
        fields = '__all__'


class DeviceInterfaceSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceInterface
        fields = '__all__'
