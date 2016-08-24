from __future__ import unicode_literals

from django.db import models

class Income(models.Model):

	CATEGORIES = (
		('sales', 'SALE OF STOCK'),
		('rent', 'RENT COLLECTION'), 
		('assets', 'SALE OF ASSETS'), 
		('tips', 'TIPS'),
		('commisions', 'COMMISION')
		)

	amount = models.IntegerField()
	category = models.CharField(choices= CATEGORIES, max_length=15) 
	currency = models.CharField(max_length=15)  
	date =  models.DateField()


	class meta:
		ordering = ['-date',]
        verbose_name = "Income"
        verbose_name_plural = "Income"