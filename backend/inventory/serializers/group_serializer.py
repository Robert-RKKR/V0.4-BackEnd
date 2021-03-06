# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.group_model import Group

# API Variable Import:
from api.variables import DEFAULT_DEPTH


# Group Serializer:
class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        depth = DEFAULT_DEPTH
        fields = '__all__'


class GroupSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'
