# Serializer Import:
from ..serializers.group_serializer import GroupSerializer
from ..serializers.group_serializer import GroupSerializerUpdateCreate

# Models Import:
from ..models.group_model import Group

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


# Group Views:
class GroupView(GenericObjectsView):

    queryset = Group
    serializer_all = GroupSerializer
    serializer_limited = GroupSerializerUpdateCreate


class GroupIdView(GenericObjectView):

    queryset = Group
    serializer_all = GroupSerializer
    serializer_limited = GroupSerializerUpdateCreate
