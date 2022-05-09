from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from . models import Customer
from .forms import CustomerForm
from django.core.paginator import Paginator, EmptyPage
# Create your views here.

def Customer_view(request):
    form = CustomerForm()
    template_name = 'custapp/custform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    return render(request, template_name, context )

def Showcustomer_view(request, page=1):
    data = Customer.objects.all()
    template_name = 'custapp/showcust.html'
    paginator = Paginator(data, 2)
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {'obj':data}
    return render(request, template_name, context)

def UpdateCustomer_view(request, id):
    data = Customer.objects.get(cid = id)
    form = CustomerForm(instance=data)
    template_name = 'custapp/custform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        form.is_valid()
        form.save()
        return redirect('show_url')
    return render(request, template_name, context)

def DeleteCustomer_view(request, id):
    data = Customer.objects.get(cid = id)
    template_name = 'custapp/delconfirm.html'
    context = {'obj': data}
    if request.method == 'POST':
        data.delete()
        return redirect('show_url')
    return render(request, template_name, context)



