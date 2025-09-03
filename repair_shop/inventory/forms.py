from django import forms
from .models import InventoryItem, PartsBasket

class Add_components(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = [
            'name',
            'part_number',
            'location',
            'category',
            'description',
            'quantity',
            'trigger',
        ]
        labels = {
            'trigger': 'Notify me reach:'
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class AddParts(forms.ModelForm):
    class Meta:
        model = PartsBasket
        fields = ['link', 'quantity', 'partnumber', 'jobnumber', 'notes']
        
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