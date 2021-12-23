# Rest Django Import:
from rest_framework import serializers

# Application Import:
from ..models.administrator_model import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Administrator
        depth = 1
        fields = [
            'id',
            'created',
            'updated',
            'last_login',
            'root',
            'active',
            'staff',
            'admin',
            'superuser',
            'username',
            'email',
            'first_name',
            'middle_name',
            'last_name',
        ]

class AdministratorPostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Administrator.objects.create_user(**validated_data)
    
    class Meta:
        model = Administrator
        fields = [
            'username',
            'password',
            'email',
        ]


# class AdministratorPostSerializer(serializers.ModelSerializer):

#     password = serializers.CharField(
#         max_length=128, min_length=8, write_only=True
#     )
    
#     class Meta:
#         model = Administrator
#         fields = [
#             'username',
#             'password',
#             'email',
#         ]

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         username = attrs.get('username', '')

#         return attrs
