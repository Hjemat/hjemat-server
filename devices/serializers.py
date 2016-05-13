from rest_framework import serializers
from devices.models import Device, DeviceCustomization

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Device
		fields = ('deviceID', 'productID', 'values')

class DeviceCustomizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeviceCustomization
		fields = ('id', 'name')
