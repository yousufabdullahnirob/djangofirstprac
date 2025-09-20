from django.shortcuts import render
from .models import Chaivarieties ,store

from django import form
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chaivarieties as chai
# views.py
from .forms import ChaivarityForm

# Create your views here.
def all_chai(request):
    chais = Chaivarieties.objects.all()  # ✅ Corrected here
    return render(request, "chai/all_chai.html", {'chais': chais})
def order_chai(request,chai_id):
    chai = get_object_or_404(chai, id=id)

    return render(request, "chai/order_page.html", {"chai": chai})

def chai_details(request, id):
    chai = get_object_or_404(Chaivarieties, id=id)
    return render(request, 'chai/chai_details.html', {'chai': chai})

def chai_store_views(request):
    stores = None
    if request.method == 'POST':
        form = ChaivarityForm(request.POST)
        if form.is_valid():
            
            chai_varity = form.cleaned_data['chai_varity']
            stores = store.object.filter (chai_varities= chai_varity)
        else:
         form = ChaivarityForm()
    return render(request, 'chai/chai_stores.html', {'form': form, 'stores': stores})