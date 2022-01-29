# Django Imports:
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Application Import:
from inventory.models.device_model import Device
from inventory.models.device_model import DeviceInterface

class DevicesStatus(APIView):

    # Generic Object GET View:
    def get(self, request, format=None):
        data = {
            'status': 'success',
            'devices': {}
        }

        try:
            data['devices']['all_devices'] = Device.objects.all().count()
            data['devices']['active_devices'] = Device.objects.filter(active=True).count()
            data['devices']['ssh_devices'] = Device.objects.filter(ssh_status=True).count()
            data['devices']['https_devices'] = Device.objects.filter(https_status=True).count()

            data['devices']['all_interfaces'] = DeviceInterface.objects.all().count()
            data['devices']['all_link_interfaces_up'] = DeviceInterface.objects.filter(link_status='up').count()
            data['devices']['all_protocol_interfaces_up'] = DeviceInterface.objects.filter(protocol_status='up').count()

            return Response(data, status=status.HTTP_200_OK)
        except:

            return Response({'status':'Fails'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
