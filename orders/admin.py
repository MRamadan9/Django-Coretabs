from django.contrib import admin
from . import models
# Register your models here.


#========== Orders Functions ==========
@admin.register(models.Order)         
class OrderAdmin(admin.ModelAdmin):
	list_display = ('product', 'user', 'created','quantity' )
	list_filter = ('user', 'product')