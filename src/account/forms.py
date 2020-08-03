from django import forms
from django.contrib.auth.forms import UserCreationForm
# Sign Up Form
from phonenumber_field.formfields import PhoneNumberField

from src.account.models import Account


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    address = forms.CharField(max_length=30)
    phone_number =  PhoneNumberField()
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = Account
        fields = [
            'username',
            'first_name',
            'last_name',
            'address',
            'phone_number',
            'email',
            'password1',
            'password2',
        ]

class LogInForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password1',
        ]

class PasswordChangeForm(UserCreationForm):
    class Meta:
        model = Account
        email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

        fields = [
            'email'
        ]
