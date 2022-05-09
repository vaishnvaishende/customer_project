from . import views
from django.urls import path
from custapp.views import Showcustomer_view


urlpatterns =[ 
    path('cv/', views.Customer_view, name='custform_url'),
    path('sc/', views.Showcustomer_view, name='show_url'),
    path('sc/<int:page>', views.Showcustomer_view, name='show_url'),
    path('uv/<int:id>' , views.UpdateCustomer_view, name='update_url'),
    path('dv/<int:id>' , views.DeleteCustomer_view, name='delete_url')
]