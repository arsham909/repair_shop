from django import forms
from .models import Repair , Company , Device

class AddRepair(forms.ModelForm):
    class Meta:
        model = Repair
        # fields = ['job_number', 'device_name']
        fields = "__all__"
        
class display_company(forms.ModelForm):
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
            'contact_person': 'Contact person',
            'is_active': 'Active',
        }
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
class Company_details(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
        labels = {
            'phonenumber' : 'Phone number',
            'postal_code': 'Postal code',
            'contact_person': 'Contact person',
            'is_active': 'active'
        }
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
        
#forms for repairs transition 
#start here
class Device_form (forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'complain': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'shipped_from': forms.Textarea(attrs={'class': 'form-control'}),
        }

class Assign_toForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['assigned_to']

    
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

