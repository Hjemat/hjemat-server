from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Device(models.Model):
	deviceID = models.IntegerField(primary_key=True)
	productID = models.IntegerField()
	values = JSONField()

class DeviceCustomization(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=32)

class Command(models.Model):
	deviceID = models.IntegerField()
	valueID = models.IntegerField()
	value = models.IntegerField()
