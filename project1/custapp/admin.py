from django.contrib import admin
from custapp.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    display_list = ['cid', 'cname', 'surname', 'email', 'gender', 'phoneno', 'address']
admin.site.register(Customer, CustomerAdmin)