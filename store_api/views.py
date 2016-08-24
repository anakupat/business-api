from django.shortcuts import render
from rest_framework import viewsets
from .models import Income
from .serializers import IncomeSerializer

from rest_framework import filters
from rest_framework import generics

class IncomeViewSet(viewsets.ModelViewSet):
    """ 
	List all Incomes in the Business or create new ones
	"""
    queryset = Income.objects.all() # Defualt behaviour
    serializer_class = IncomeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category',)