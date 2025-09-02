from django import forms
from .models import Repair , Company , Device , Client

class AddRepair(forms.ModelForm):
    class Meta:
        model = Repair
        # fields = ['job_number', 'device_name']
        fields = "__all__"

class Client_Create_form(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

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
        fields = [
            'name',
            'phonenumber',
            'email',
            'address',
            'postal_code',
            'contact_person',
            'client',
            'notes',
        ]
        
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
        fields = [
            'brand',
            'device_name',
            'part_number',
            'serial_number',
            'description',
            'shipped_from',
            'postal_code',
            'phone_numnber',
            'complain',
            'created_by',
        ]
        widgets = {
            'complain': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'shipped_from': forms.Textarea(attrs={'class': 'form-control'}),
        }

class Assign_Form(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'job_number',
            'assigned_to',
            'complain',
            'client',
            'rush',
            ]
class Repairs_list(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'device',
            'state',
            
        ]


class Evaluating(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'parts_needs',
            'can_test',
            'evaluating_notes',
            'parts_total_price',
            
        ]
        # widgets = {
        #     'parts_needs' : forms.CheckboxSelectMultiple,
        #     }

class Qouting_form(forms.ModelForm):
    class Meta:
        model = Repair
        fields= [
            'qouting_notes'
        ]

class Approved_form(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'customer_respond'
        ]
class Repairing_form(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'parts_needs',
            'video',
            'how_fixed',
            'repaired_notes',
        ]
        
class Shipper_form(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'shipper_note'
        ]
        
class Shipped_form(forms.ModelForm):
    class Meta:
        model = Repair
        fields = [
            'tracking_number'
        ]
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

