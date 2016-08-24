from django.contrib import admin
from . models import Income
# Register your models here.

class IncomeAdmin(admin.ModelAdmin):
	list_display = ('amount', 'category', 'currency', 'date')

admin.site.register(Income, IncomeAdmin)