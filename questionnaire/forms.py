from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from .models import *


class DeptInfoForm(ModelForm):
    class Meta:
        model = DeptInfo
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {
            "ta_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "ta_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "ta_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            "eur_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "eur_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "eur_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            "ds_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "ds_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "ds_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
        }


class VendInfoForm(ModelForm):

    CHOICES = [("Yes", "Yes"), ("No", "No"), ("Under Negotiation", "Under Negotiation")]

    exst_contract = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(attrs={"class": "form-check"})
    )

    class Meta:
        model = VendInfo
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {
            "tc_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "tc_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "tc_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
        }


class DataManagementForm(ModelForm):
    class Meta:
        model = DataManagement
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class AvailabiltyCriticalityForm(ModelForm):
    class Meta:
        model = AvailabiltyCriticality
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class ComplianceForm(ModelForm):
    class Meta:
        model = Compliance
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class SecMatEvidenceForm(ModelForm):
    class Meta:
        model = SecMatEvidence
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class IntegrationForm(ModelForm):
    class Meta:
        model = Integration
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class CloudServiceForm(ModelForm):
    class Meta:
        model = CloudService
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class SecureDesignForm(ModelForm):
    class Meta:
        model = SecureDesign
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class EncryptionForm(ModelForm):
    class Meta:
        model = Encryption
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class QAEnvironmentForm(ModelForm):
    class Meta:
        model = QAEnvironment
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class DatabaseServersForm(ModelForm):
    class Meta:
        model = DatabaseServers
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class SecureCommsForm(ModelForm):
    class Meta:
        model = SecureComms
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}


class SWIntegrityForm(ModelForm):
    class Meta:
        model = SWIntegrity
        fields = "__all__"
        exclude = ["project", "vend_has_perm"]
        widgets = {}
