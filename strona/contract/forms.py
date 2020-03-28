from django import forms
from .models import Contract
from blog.models import Post

class ContractForm(forms.ModelForm): 
    expires_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Contract
        exclude = ['client', 'executor', 'post']
