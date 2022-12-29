from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Contact


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'type': 'text', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
                            'name':'username', 'placeholder':'Your Username'
        })
        self.fields["email"].widget.attrs.update({
            'type': 'text', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
            'name': 'email', 'placeholder': 'Your Email'
        })
        self.fields["password1"].widget.attrs.update({
            'type': 'password', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
            'name': 'password1', 'placeholder': 'Password'
        })
        self.fields["password2"].widget.attrs.update({
            'type': 'password', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
            'name': 'password2', 'placeholder': 'Confirm Password'
        })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Loginform(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(Loginform, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
                            'name':'username', 'placeholder':'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password', 'class': 'woocommerce-Input woocommerce-Input--text input-text form-control',
            'name': 'password1', 'placeholder': 'Password'}
    ))
    class Meta:
        model = User
        fields = ['username', 'password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact', 'subject', 'message', 'policy']
        widgets = {
            'name': forms.TextInput(
                attrs={'type': 'text', 'name': "name", 'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required form-control',
                       'size':40,'aria-required':True,'aria-invalid':False,'placeholder': 'Your Name'}),
            'email': forms.TextInput(
                attrs={'type': 'email', 'name': "email",
                       'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required form-control',
                       'size': 40, 'aria-required': True, 'aria-invalid': False, 'placeholder': 'Your Email'}),
            'contact': forms.TextInput(
                attrs={'type': 'text', 'name': "contact",
                       'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required form-control',
                       'size': 40, 'aria-required': True, 'aria-invalid': False, 'placeholder': 'Your Number'}),
            'subject': forms.TextInput(
                attrs={'type': 'text', 'name': "subject",
                       'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required form-control',
                       'size': 40, 'aria-required': True, 'aria-invalid': False, 'placeholder': 'Your Subject'}),
            'message': forms.Textarea(
                attrs={'type': 'text', 'name': "message",
                       'class': 'wpcf7-form-control wpcf7-text wpcf7-validates-as-required form-control',
                       'size': 40, 'aria-required': True, 'aria-invalid': False, 'placeholder': 'Message'}),

        }









