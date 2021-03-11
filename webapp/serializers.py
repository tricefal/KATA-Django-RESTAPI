from django.db.models import fields
from rest_framework import serializers
from . models import employees

class EmployeesSerializers(serializers.ModelSerializer):

	class Meta:
		model = employees
		fields = ('firstname', 'lastname')
		# fields = "__all__"

