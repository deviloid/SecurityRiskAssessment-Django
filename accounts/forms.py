from django import forms
from django.forms.models import ModelForm
from .models import Account
from project.models import Project
from vendor.models import Vendor, UserVendor
from department.models import Department, UserDepartment
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label="Test",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
                "type": "email",
                "name": "email",
            }
        ),
    )


class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        ),
    )
    new_password2 = forms.CharField(
        label="Conform Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        ),
    )


class SignUpForm(ModelForm):
    class Meta:
        model = Account
        fields = ["fname", "lname", "email"]
        widgets = {
            "fname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "lname": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "example@abc.xyz"}
            ),
        }


class DeptCreateForm(ModelForm):

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Department",
    )

    class Meta:
        model = UserDepartment
        fields = ["department", "phone"]
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            )
        }


class VendCreateForm(ModelForm):

    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Vendor",
    )

    class Meta:
        model = UserVendor
        fields = ["vendor", "phone"]
        widgets = {
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            )
        }


class ProjectCreateForm(ModelForm):
    risk_analyst = forms.ModelChoiceField(
        label='Risk Analyst',
        queryset=Account.objects.filter(is_staff=True),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Risk Analyst",
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Department",
    )
    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Vendor",
    )
    dept_mpc = forms.ModelChoiceField(
        label='Main Project Contact (Dept)',
        queryset=UserDepartment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Main Project Contact (Dept)",
    )
    vend_mpc = forms.ModelChoiceField(
        label='Main Project Contact (Vendor)',
        queryset=UserVendor.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Main Project Contact (Vendor)",
    )

    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Project Name"}
            ),
            "purpose": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Project Purpose"}
            ),
        }