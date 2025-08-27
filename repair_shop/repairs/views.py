from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import CreateView, FormView, TemplateView , UpdateView, DetailView, ListView
from .models import Repair , Company , Client , Device
from .forms import Client_Create_form, display_company , Company_details , make_form_readonly , Device_form, Assign_Form
# Create your views here.

class Repairs_list(ListView):
    model = Repair
    paginate_by = 25
    template_name = 'repairs/job/repairs_list.html'
    # context_object_name = 'repairs'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['checked_in'] = Repair.objects.filter(state ='checked_in')
        context['repairs'] = Repair.objects.exclude(state ='checked_in' )
        return context
        
#veiw for add repair
class CheckIn(CreateView):
    model=Repair
    form_class = Device_form
    template_name = 'repairs/job/checkin_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Device_form'] = Device_form()
        return context
    
    def post(self, request, *args, **kwargs):
        Device_input = Device_form(request.POST)
        repair = Repair()
        if Device_input.is_valid():
            # Device_input.instance.created_by=request.user
            new_device = Device_input.save()
            repair.device = new_device
            repair.move_to_checkin()
            repair.save()
            return redirect('repairs:repairs')
    
class assign_requested(UpdateView):
    model = Repair
    form_class = Assign_Form
    template_name = 'repairs/job/assign_request_form.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['Assign_Form'] = Assign_Form()
        return context
    def post(self, request , *args, **kwargs):
        return

#Device class base view
class Device_list(ListView):
    model = Device
    template_name = 'repairs/device/device_list.html'
    context_object_name = 'devices'
    
#client class view (create list ,detail , edit)
class ClientCreateView(CreateView):
    model = Repair
    form_class = Client_Create_form
    template_name = 'repairs/client/client_create_form.html'
    success_url = '/repairs/clients'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_form'] = Client_Create_form()
        return context

    def post(self, request, *args, **kwargs):
        new_client = Client_Create_form(request.POST)
        if new_client.is_valid():
            new_client.save()
            return redirect('repairs:clients_list')
        return render(request, 'repairs/client/client_create_form.html')

class Clients(TemplateView):
    template_name = 'repairs/client/clients_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['client_form'] = Client_Create_form()
        return context

class ClientDetailView(DetailView):
    model = Client
    template_name = 'repairs/client/client_detail.html'
    fields ='__all__'
    # success_url = '/repairs/job/list'
    
    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        client_instance = self.object
        context['client_detail'] = client_instance
        context['client_form'] = make_form_readonly(Client_Create_form(instance=client_instance))
        return context

class ClientEditView(UpdateView):
    model = Client
    template_name = 'repairs/client/client_create_form.html'
    success_url = '/repairs/clients'
    fields ='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_instance = self.object
        context['client_detail'] = client_instance
        context['client_form'] = Client_Create_form(instance=client_instance)
        return context

def jobs(request):
    # MBVs = RepairJobs.MBV.all()
    # print(dir(request.user))
    jobs = Repair.objects.all()
    print(jobs)
    return render(
        request, 'repairs/job/list.html', {'jobs':jobs})

def list_companies(request):
    list = Company.objects.all().filter(is_active='True')
    form = display_company()
    return render(request, 'repairs/company/company_list.html', {'list':list , 'form':form})

def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    form = Company_details(instance=company)
    form = make_form_readonly(form)
    return render(request, 'repairs/company/company_detail.html', {'form':form , 'company':company})

def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    form = Company_details(instance=company)
    if request.method == "POST":
        form = Company_details(request.POST, instance=company)
        if form.is_valid():
            form.save()
        return redirect(company.get_absolute_url())
    else:
        form = Company_details(instance=company)
    return render(request, 'repairs/company/AddCompany.html' , {'form':form})

def compnay_delete(request, pk):
    if request.method == "POST":
        company = get_object_or_404(Company, pk=pk)
        company.is_active = False
        company.save(update_fields=['is_active'])
        messages.success(request, 'Company deleted successfully!')
        response = HttpResponse(status=204)
        response["HX-Redirect"] = reverse('repairs:companies_list')
    return response

def AddCompany_view(request):
    
    if request.method == "POST":
        form = Company_details(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/repairs/thanks/")
    else:
        form = Company_details()
    return render(request, "repairs/company/AddCompany.html", {"form": form})

def search_company(request):
    query = request.GET.get('search_company', '')
    companies = Company.objects.filter(is_active=True)
    form = display_company()
    if query:
        companies = Company.objects.filter(
        Q(name__icontains=query) |
        Q(address__icontains=query) |
        Q(phonenumber__icontains=query) |
        Q(contact_person__icontains=query) |
        Q(postal_code__icontains=query) |
        Q(email__icontains=query) 
            )
    companies = companies.order_by('name')
    return render(request,'repairs/company/partials/SearchCompany.html', {'list': companies, 'form':form})

# @login_required
# def AddRepairs(request):
#     if request.method == "POST":
#         form = AddRepair(request.POST)
#         if form.is_valid():
#             form.save()
#             # print(form)
#         return HttpResponseRedirect("/repairs/thanks/")
#     else:
#         form = AddRepair()
#         # print(form)
#     return render(request , "repairs/job/AddRepairs.html", {"form": form})


def thanks(request):
    return render(request, 'repairs/job/thanks.html', )