from django.shortcuts import render
from .models import InventoryItem
# Create your views here.

def inventory(request):
    to_buy = InventoryItem.to_buy.all()
    return render(request,'inventory/items/list.html', {'to_buy': to_buy})