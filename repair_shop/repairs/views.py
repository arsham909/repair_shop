from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import RepairJobs , Company
from .forms import AddRepair, AddCompany

# Create your views here.
def jobs(request):
    MBVs = RepairJobs.MBV.all()
    return render(
        request, 'repairs/job/list.html',
        {'MBVs': MBVs}
    )
    
    
def AddCompany_view(request):
    
    if request.method == "POST":
        form = AddCompany(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/repairs/thanks/")
    else:
        form = AddCompany()
    return render(request, "repairs/job/AddCompany.html", {"form": form})
    
def AddRepairs(request):
    if request.method == "POST":
        form = AddRepair(request.POST)
        if form.is_valid():
            form.save()
            print(form)
        return HttpResponseRedirect("/repairs/thanks/")
    else:
        form = AddRepair()
        print(form)
    return render(request , "repairs/job/AddRepairs.html", {"form": form})

def thanks(request):
    return render(request, 'repairs/job/thanks.html', )