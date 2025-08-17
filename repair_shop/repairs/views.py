from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import RepairJobs , Company
from .forms import AddRepair, AddCompany
from django.contrib.auth.decorators import login_required

# Create your views here.

def jobs(request):
    # MBVs = RepairJobs.MBV.all()
    # print(dir(request.user))
    # jobs = request.user.Repairs.all()
    return render(
        request, 'repairs/job/list.html')

def list_companies(request):
    list = Company.objects.all()
    form = AddCompany()
    print(list)
    return render(request, 'repairs/company/company_list.html', {'list':list , 'form':form})

def companies_detail(request, pk):
    return 

@login_required
def AddCompany_view(request):
    
    if request.method == "POST":
        form = AddCompany(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/repairs/thanks/")
    else:
        form = AddCompany()
    return render(request, "repairs/company/AddCompany.html", {"form": form})

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