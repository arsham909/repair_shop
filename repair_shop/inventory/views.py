from django.shortcuts import render , redirect , HttpResponseRedirect , HttpResponse
from .models import InventoryItem
from .forms import Add_components
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def inventory(request):
    to_buy = InventoryItem.to_buy.all().order_by('category', 'quantity')
    all = InventoryItem.to_buy.quantity()
    
    return render(request,'inventory/items/list.html', {'to_buy': to_buy, 'all': all})

def add_components(request):
    if request.method == 'POST':
        form = Add_components(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Component added successfully!')
        return HttpResponseRedirect('/inventory/')
    else:
        form = Add_components()
    return render(request, 'inventory/items/AddComponents.html', {'form': form} )

def edit_components(request):
    
    return 

def thanks(request):
    return render(request, 'inventory/items/thanks.html', )


def searchcomponent(request):
    query = request.GET.get('searchcomponent1', '')
    
    components = InventoryItem.objects.filter(
    Q(name__icontains=query) |
    Q(part_number__icontains=query) |
    Q(description__icontains=query) |
    Q(location__icontains=query) |
    Q(category__icontains=query)
        ).order_by('category', 'quantity')
    
    return render(request,'inventory/partials/searchcomponent.html', {'to_buy': components})
