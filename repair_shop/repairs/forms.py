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
        fields = [
            'name',
            'phonenumber',
            'email',
            'address',
            'postal_code',
            'contact_person',
        ]
        labels = {
            'phonenumber' : 'Phone number',
            'postal_code': 'Postal code',
            'contact_person': 'Contact person'
        }
        
def make_form_readonly(form):
    """
    Loops through form fields and makes them read-only/disabled.
    - readonly: user can still select & copy text
    - disabled: prevents changes & form submission of the field
    """
    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
        field.widget.attrs['disabled'] = True
    return form