from django import forms
from .models import RepairJobs

class AddRepair(forms.ModelForm):
    class Meta:
        model = RepairJobs
        # fields = ['job_number', 'device_name']
        fields = "__all__"