from django.shortcuts import render
from .models import RepairJobs

# Create your views here.
def jobs(request):
    MBVs = RepairJobs.MBV.all()
    return render(
        request, 'repairs/job/list.html',
        {'MBVs': MBVs}
    )