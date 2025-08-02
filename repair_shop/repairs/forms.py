from django import forms
from .models import RepairJobs , Company

class AddRepair(forms.ModelForm):
    class Meta:
        model = RepairJobs
        # fields = ['job_number', 'device_name']
        fields = "__all__"
        
class AddCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"