from django import forms
from django.contrib.auth.models import User
from .models import Contract, Offer, Request
from blog.models import Post
from users.models import Profile


class ContractForm(forms.ModelForm):
    expires_date = forms.DateField(widget=forms
                                   .TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Contract
        exclude = ['client', 'executor', 'post']


class OfferForm(forms.ModelForm):

    def __init__(self, client, user_id, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        offer_request = Request.objects.filter(applicant_id=user_id)
        self.fields['post'].queryset = (Post
                                        .objects
                                        .filter(author=client,
                                                request__in=offer_request))
        self.fields['executor'].widget = forms.HiddenInput()
    deadline = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    offer_id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Offer
        exclude = ['client', 'status']
