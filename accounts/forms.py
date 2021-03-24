from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from department.models import UserDepartment
from vendor.models import UserVendor
from.models import Account

class DepartmentSignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Confirm Password'}))
    

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['fname', 'lname', 'email', 'password1', 'password2']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'register-form-field', 'placeholder': 'example@abc.xyz'}),           
            }
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_userdepartment = True
        user.save()
        udept = UserDepartment.objects.create(user=user)
        return user

class VendorSignUpForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['fname', 'lname', 'email', 'password1', 'password2']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'register-form-field', 'placeholder': 'example@abc.xyz'}),           
            }
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_uservendor = True
        user.save()
        uvendor = UserVendor.objects.create(user=user)
        return user
