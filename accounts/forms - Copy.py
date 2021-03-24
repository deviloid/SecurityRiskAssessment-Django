from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.db import transaction
from department.models import UserDepartment
from vendor.models import UserVendor
from.models import Account

# class DepartmentSignUpForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = Account
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_userdepartment = True
#         user.save()
#         udept = UserDepartment.objects.create(user=user)
#         return user

# class VendorSignUpForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = Account
    
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_uservendor = True
#         user.save()
#         uvendor = UserVendor.objects.create(user=user)
#         return user

# class CreateUserForm(UserCreationForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Confirm Password'}))
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'class': 'register-form-field', 'placeholder': 'example@abc.xyz'}),           
#             }

# class SignUpForm(UserCreationForm):
#     username = forms.EmailField(forms.EmailInput(attrs={'class': 'register-form-field', 'placeholder': 'example@abc.xyz'}))
#     email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email','placeholder': _('E-mail address')}))
#     fname = forms.CharField(forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
#     lname=forms.CharField(forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
#     email=forms.EmailField(forms.EmailInput(attrs={'class': 'register-form-field', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
#     password1=forms.CharField(forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Password'}))
#     password2=forms.CharField(forms.PasswordInput(attrs={'class': 'register-form-field', 'placeholder': 'Confirm Password'}))

#     class Meta(UserCreationForm.Meta):
#         model = User
# #       I've tried both of these 'fields' declaration, result is the same
#         fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
#         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'register-form-field', 'placeholder': 'Username'}),
#         }