from django import forms
from django.forms.models import ModelForm, model_to_dict
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

from .widgets import RadioSelectButtonGroup
from .models import Account
from product.models import Product
from vendor.models import Vendor, UserVendor
from department.models import Department, UserDepartment
from riskassessment.models import RiskAssessment


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


class ProductCreateForm(ModelForm):
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
    dept_mpc = forms.ModelChoiceField(
        label='Main Project Contact (Dept)',
        queryset=UserDepartment.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Main Project Contact (Dept)",
    )
    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Vendor",
    )
    vend_mpc = forms.ModelChoiceField(
        label='Main Project Contact (Vendor)',
        queryset=UserVendor.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select Main Project Contact (Vendor)",
    )

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['slug']
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Project Name"}
            ),
            "purpose": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Project Purpose"}
            ),
        }
    field_order = ['name', 'purpose', 'risk_analyst', 'department', 'dept_mpc', 'vendor', 'vend_mpc']


class DepartmentCreateForm(ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'})
        }


class VendorCreateForm(ModelForm):
    CHOICES = [
        ('Yes','Yes'),
        ('No','No'),
        ('Under Negotiation','Under Negotiation')
    ]
    exstContract = forms.ChoiceField(choices=CHOICES, widget=RadioSelectButtonGroup(), label='Do you have an existing signed contract with the Company?')

    class Meta:
        model = Vendor
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vendor Name'}),
            'website':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website'})
        }


class CreateRAForm(ModelForm):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={'class':'form-control'}), empty_label="Select Product",)

    class Meta:
        model = RiskAssessment
        fields = ['product']
