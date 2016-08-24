from rest_framework import serializers
from store_api.models import Income

class IncomeSerializer( serializers.ModelSerializer ):
	"""Serializer to parse Task data"""

	class Meta:
		model = Income


