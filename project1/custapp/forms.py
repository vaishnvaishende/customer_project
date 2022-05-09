from tkinter import Widget
from django import forms
from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels ={
            'cid': 'CUSTOMER ID',
            'cname': 'NAME',
            'surname': 'SURNAME',
            'email': 'EMAIL ID',
            'gender': 'GENDER',
            'phoneno': 'PHONE NO',
            'address': 'ADDRESS'
        }
        