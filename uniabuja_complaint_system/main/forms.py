from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('name', 'complaint')
        labels = {
            'name': 'Full name',
            'complaint': ' Complaint',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name (or leave blank to remain anonymous)',  'class': 'form-control'}),
            'complaint': forms.Textarea(attrs={'placeholder': 'Enter complaint here', 'class': 'form-control'}),
        }