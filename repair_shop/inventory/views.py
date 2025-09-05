from django.shortcuts import render , redirect , HttpResponseRedirect , get_object_or_404 
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages 
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, ListView
from .models import InventoryItem , PartsBasket
from .forms import Add_components , make_form_readonly , AddParts, OrderedParts
# Create your views here.

class PartsBasketList(ListView):
    model = PartsBasket
    template_name = 'inventory/basket/parts_list.html'
    paginate_by = 25
    context_object_name = 'parts'
class PartsBasketCreate(CreateView):
    model = PartsBasket
    template_name = 'inventory/basket/add_parts.html'
    context_object_name = 'basket'
    form_class = AddParts
    success_url = reverse_lazy('inventory:basket_list')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['partform'] = AddParts()
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     part = self.form_class(request.POST)
    #     parts_basket = PartsBasket()
    #     if part.is_valid():
    #         parts = part.save()
    #         parts_basket = parts
    #         parts_basket.save()
    #         return redirect('inventory:basket_list')

class PartsBasketEdit(UpdateView):
    model = PartsBasket
    template_name = 'inventory/basket/edit_part.html'
    context_object_name = 'basket'
    form_class = OrderedParts
    success_url = reverse_lazy('inventory:basket_list')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['partform'] = OrderedParts()
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     part = self.form_class(request.POST)
    #     parts_basket = OrderedParts()
    #     if part.is_valid():
    #         parts = part.save()
    #         parts_basket = parts
    #         parts_basket.save()
    #         return redirect('inventory:basket_list')
    

# def Part_Edit(request, pk):
#     part = get_object_or_404(PartsBasket, pk=pk)
#     if request.method == 'POST':
#         form = OrderedParts(request.POST, instance=part)
#         if form.is_valid():
#             form.save()
#             return redirect('inventory:basket_list')
#     else:
#         form = OrderedParts(instance=part)
#     return render(request, 'inventory/basket/edit_part.html', {'form':form})


def inventory(request):
    to_buy = InventoryItem.to_buy.filter(is_active='True').order_by('category', 'quantity')
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

def component_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    form = Add_components(instance=item)
    form = make_form_readonly(form)
    return render(request, 'inventory/items/component.html', {'form': form , 'item':item})

def component_edit(request , pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = Add_components(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(item.get_absolute_url())
    else:
        form = Add_components(instance=item)
    return render (request, 'inventory/items/AddComponents.html', {'form': form} )

def component_delete(request , pk):
    if request.method == 'POST':
        item = get_object_or_404(InventoryItem, pk=pk)
        item.is_active = False
        item.save(update_fields=['is_active'])
        messages.success(request, 'Component deleted successfully!')
        response = HttpResponse(status=204)
        response["HX-Redirect"] = reverse('inventory:inventory')  # ← Magic header
        return response

def thanks(request):
    return render(request, 'inventory/items/thanks.html', )

def searchcomponent(request):
    query = request.GET.get('searchcomponent1', '')
    components = InventoryItem.objects.filter(is_active=True)
    if query:
        components = InventoryItem.objects.filter(
        Q(name__icontains=query) |
        Q(part_number__icontains=query) |
        Q(description__icontains=query) |
        Q(location__icontains=query) |
        Q(category__icontains=query)
            ).order_by('category', 'quantity')
    components = components.order_by('category', 'quantity')
    return render(request,'inventory/partials/searchcomponent.html', {'to_buy': components})


