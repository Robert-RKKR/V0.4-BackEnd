# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.policy_manager_model import PolicyManager

# API Variable Import:
from api.variables import DEFAULT_DEPTH


class PolicyManagerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PolicyManager
        depth = DEFAULT_DEPTH
        fields = '__all__'


class PolicyManagerSerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = PolicyManager
        fields = '__all__'
