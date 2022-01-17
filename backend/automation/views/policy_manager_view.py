# Serializer Import:
from ..serializers.policy_manager_serializer import PolicyManagerSerializer
from ..serializers.policy_manager_serializer import PolicyManagerSerializerUpdateCreate

# Models Import:
from ..models.policy_manager_model import PolicyManager

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


# Policy Views:
class PolicyManagerView(GenericObjectsView):

    queryset = PolicyManager
    serializer_all = PolicyManagerSerializer
    serializer_limited = PolicyManagerSerializerUpdateCreate
    allowed_methods = ['get']


class PolicyManagerIdView(GenericObjectView):

    queryset = PolicyManager
    serializer_all = PolicyManagerSerializer
    serializer_limited = PolicyManagerSerializerUpdateCreate
    allowed_methods = ['get', 'delete']
