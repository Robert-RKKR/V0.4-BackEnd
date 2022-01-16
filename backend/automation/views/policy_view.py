# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.policy_serializer import PolicySerializer
from ..serializers.policy_serializer import PolicySerializerUpdateCreate

# Models Import:
from ..models.policy_model import Policy

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


# Policy Views:
class PolicyView(GenericObjectsView):

    queryset = Policy
    serializer_all = PolicySerializer
    serializer_limited = PolicySerializerUpdateCreate


class PolicyIdView(GenericObjectView):

    queryset = Policy
    serializer_all = PolicySerializer
    serializer_limited = PolicySerializerUpdateCreate
