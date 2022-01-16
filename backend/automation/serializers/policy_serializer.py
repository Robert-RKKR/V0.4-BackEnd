# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.policy_model import Policy

# API Variable Import:
from api.variables import DEFAULT_DEPTH


class PolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Policy
        depth = DEFAULT_DEPTH
        fields = '__all__'


class PolicySerializerUpdateCreate(serializers.ModelSerializer):
    
    class Meta:
        model = Policy
        fields = '__all__'
