from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from devices.models import DeviceCustomization
from devices.serializers import DeviceCustomizationSerializer

@api_view(['GET', 'POST'])
def dc_list(request, format=None):
    """
    List all devices, or create a new device.
    """
    if request.method == 'GET':
        dcs = DeviceCustomization.objects.all()
        serializer = DeviceCustomizationSerializer(dcs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceCustomizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dc_detail(request, pk, format=None):
    """
    Retrieve, update or delete a device instance.
    """
    try:
        dc = DeviceCustomization.objects.get(id=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeviceCustomizationSerializer(dc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeviceCustomizationSerializer(dc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
