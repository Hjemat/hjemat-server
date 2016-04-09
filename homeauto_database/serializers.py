from rest_framework import serializers
from homeauto_database.models import Device

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Device
		fields = ('id', 'deviceID', 'productID', 'values')
