from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Device(models.Model):
	deviceID = models.IntegerField()
	productID = models.IntegerField()
	values = JSONField()

class Command(models.Model):
	deviceID = models.IntegerField()
	valueID = models.IntegerField()
	value = models.IntegerField()
