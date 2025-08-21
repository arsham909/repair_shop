from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect , HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Repair , Company
from .forms import AddRepair, display_company , Company_details , make_form_readonly
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def jobs(request):
    # MBVs = RepairJobs.MBV.all()
    # print(dir(request.user))
    # jobs = request.user.Repairs.all()
    return render(
        request, 'repairs/job/list.html')

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

@login_required
def AddRepairs(request):
    if request.method == "POST":
        form = AddRepair(request.POST)
        if form.is_valid():
            form.save()
            # print(form)
        return HttpResponseRedirect("/repairs/thanks/")
    else:
        form = AddRepair()
        # print(form)
    return render(request , "repairs/job/AddRepairs.html", {"form": form})

def thanks(request):
    return render(request, 'repairs/job/thanks.html', )