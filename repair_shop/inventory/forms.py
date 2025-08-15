from django import forms
from .models import InventoryItem

class Add_components(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'