from django import forms
from .models import Order


class Checkout_Form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company_name', 'country', 'street_address', 'city','postcode', 'phone_number', 'email','additional_info']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'type': 'text', 'name': "billing_first_name",'autocomplete':"given-name",
                       'class': 'input-text form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'type': 'text', 'name': "billing_last_name", 'autocomplete': "given-name",
                       'class': 'input-text form-control', 'placeholder': 'Last Name'}),
            'company_name': forms.TextInput(
                attrs={'type': 'text', 'name': "billing_company_name", 'autocomplete': "given-name",
                       'class': 'input-text form-control', 'placeholder': 'Company Name'}),
            'country': forms.Select(
                attrs={'type': '', 'name': "billing_company_name", 'autocomplete': "country","style":"display: none;",'tabindex':"-1", 'aria-hidden':"true",
                       'class':'country_to_state country_select form-control select2-hidden-accessible', "data-placeholder":"Select a country / region…",'data-label':"Country / Region"}),


        }