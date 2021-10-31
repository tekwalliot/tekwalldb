import django_filters
from django import forms
from django.db import models
from django_filters import DateFilter

from .models import *

class OrdersFilter(django_filters.FilterSet):
	
	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		# for _, value in self.form.fields.items():
  		# 	value.widget.attrs['placeholder'] = value.help_text
  		for field in self.form.fields:
  			self.form.fields[field].widget.attrs.update({'class': 'form-control'})
	
	from_date 	= DateFilter(field_name='Order_Date', lookup_expr='gte')
	to_date 	= DateFilter(field_name='Order_Date', lookup_expr='lte')

	# Order_Details = django_filters.CharFilter(field_name='Order_Details', widget=forms.TextInput(attrs={
 #            'placeholder': 'Search place', 'class': 'form-control'}))
 	# Company_Name = django_filters.CharFilter(field_name='Company_Name', widget= {'class': 'form-control'})
	

	class Meta:
		model 	= Orders
		# fields 	= '__all__'
		# exclude = ['Order_No']
		# fields = {"Order_Date":['gte', 'lte'], "Order_Value":['gte', 'lte']}
		# "Order_Details": ['icontains']
		fields = ['Company_Name', 'Is_Confirmed']
		# filter_overrides = {
  #       models.CharField: {
  #           'filter_class': django_filters.CharFilter,
  #           'extra': lambda f: {
  #               'lookup_expr': 'icontains',
  #               'widget': forms.TextInput(attrs={'class': 'form-control'})
  #           },
  #       }}


class ExpensesFilter(django_filters.FilterSet):
	
	def __init__(self, *args, **kwargs):
  		super().__init__(*args, **kwargs)
  		for field in self.form.fields:
  			self.form.fields[field].widget.attrs.update({'class': 'form-control'})
	
	from_date 	= DateFilter(field_name='Date', lookup_expr='gte')
	to_date 	= DateFilter(field_name='Date', lookup_expr='lte')	

	class Meta:
		model 	= Expenses
		fields = ['CompanyName', 'Category']

   