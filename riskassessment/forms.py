from django import forms
from django.db.models import query
from django.forms.models import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes 

# from bootstrap4.widgets import RadioSelectButtonGroup
from accounts.widgets import RadioSelectButtonGroup, CheckboxInputGroup

from .models import *


class DeptInfoForm(ModelForm):
    mpc = forms.ModelChoiceField(queryset=UserDepartment.objects.none(), widget=forms.Select(attrs={'class':'form-control'}))
    ta_dept = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), empty_label="Select Technical Administrator Department")
    eur_dept = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), empty_label="Select End-User Requestor Department")
    ds_dept = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), empty_label="Select Data Steward Department")

    # def __init__(self, *args, **kwargs):
    #     super(DeptInfoForm, self).__init__(*args, **kwargs)
    #     self.fields['mpc'].queryset = UserDepartment.objects.filter(department_id=Product.department_id)

    class Meta:
        model = DeptInfo
        fields = "__all__"
        exclude = ["vend_has_perm", "score", "max_score", "eval_score"]
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['exst_contract'].disabled = True
        self.fields['mpc_name'].disabled = True
        self.fields['mpc_email'].disabled = True
        self.fields['mpc_phone'].disabled = True
        self.fields['exst_contract'].label = False
        self.helper.layout = Layout(
            Div(InlineRadios('exst_contract')),
        )

    class Meta:
        model = VendInfo
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "mpc_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "mpc_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "mpc_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            "tc_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "tc_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "tc_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone"}
            ),
            "vend_has_perm": forms.CheckboxInput()
        }
    

class DataManagementForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    INT_CHOICES = [
        (None,'Select Option'),
        (500, 500),
        (1000, 1000),
        (2000, 2000),
        (3000, 3000),
        (4000, 4000),
        (5000, 5000),
        (6000, 6000),
        (7000, 7000),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['reg_data'].label = False
        self.fields['data_classi'].label = False
        self.fields['recs_purged'].label = False
        self.fields['data_process_outside'].label = False
        self.fields['data_stored_outside'].label = False
        self.fields['data_rcvd_outside'].label = False
        self.fields['data_accss_outside'].label = False
        self.helper.layout = Layout(
            InlineCheckboxes('reg_data'),
            InlineCheckboxes('data_classi'),
            InlineRadios('recs_purged'),
            InlineRadios('data_process_outside'),
            InlineRadios('data_stored_outside'),
            InlineRadios('data_rcvd_outside'),
            InlineRadios('data_accss_outside'),
        )


    reg_data = forms.ModelMultipleChoiceField(
        queryset=RegulatedData.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    data_classi = forms.ModelMultipleChoiceField(
        queryset=DataClassification.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    recs_in_data = forms.ChoiceField(
        choices=INT_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )
    recs_purged = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.RadioSelect(),
        label="Are records purged from Data?",
    )
    est_add_recs = forms.ChoiceField(
        choices=INT_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )
    data_process_outside = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.RadioSelect(),
        label="Is data processing performed outside the US?",
    )
    data_stored_outside = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.RadioSelect(),
        label="Is data stored outside the US?",
    )
    data_rcvd_outside = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.RadioSelect(),
        label="Is any data received (directly or indirectly by the Company) from individuals outside of the US?",
    )
    data_accss_outside = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=forms.RadioSelect(),
        label="Are data or Systems accessible outside the US?",
    )

    class Meta:
        model = DataManagement
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class AvailabiltyCriticalityForm(ModelForm):

    A_CHOICES = [("Tier 1", "Tier 1"), ("Tier 2", "Tier 2"), ("Tier 3", "Tier 3")]
    C_CHOICES = [("High", "High"), ("Medium", "Medium"), ("Low", "Low")]

    a_rating = forms.ChoiceField(
        choices=A_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )
    c_rating = forms.ChoiceField(
        choices=C_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = AvailabiltyCriticality
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class ComplianceForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['sso'].label = False
        self.fields['audit_req_std_comp'].label = False
        self.fields['auto_patch'].label = False
        self.helper.layout = Layout(
            InlineRadios('sso'),
            InlineRadios('audit_req_std_comp'),
            InlineRadios('auto_patch'),
        )

    sso = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Single Sign-on Systems?",
    )
    audit_req_std_comp = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Company System Audit Requirements Standard Compliant?",
    )
    auto_patch = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Vendor Provides automated patching?",
    )

    class Meta:
        model = Compliance
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class SecMatEvidenceForm(ModelForm):
    
    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['attst_o_comp'].label = False
        self.fields['soc2_reports'].label = False
        self.fields['ann_pen_scan_results'].label = False
        self.fields['ann_wa_vuln_scan'].label = False
        self.helper.layout = Layout(
            InlineRadios('attst_o_comp'),
            InlineRadios('soc2_reports'),
            InlineRadios('ann_pen_scan_results'),
            InlineRadios('ann_wa_vuln_scan'),
        )

    attst_o_comp = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Attestation of Compliance",
    )
    soc2_reports = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Current system’s vendor 3rd party SOC2 Type 2 reports",
    )
    ann_pen_scan_results = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Annual penetration/vulnerability scanning results of all system components",
    )
    ann_wa_vuln_scan = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Annual web application vulnerability scan of all system web applications",
    )

    class Meta:
        model = SecMatEvidence
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class IntegrationForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['sso'].label = False
        self.fields['mfa'].label = False
        self.fields['adfs'].label = False
        self.helper.layout = Layout(
            InlineRadios('sso'),
            InlineRadios('mfa'),
            InlineRadios('adfs'),
        )

    sso = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Single Sign-on",
    )
    mfa = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Multi-Factor Authentication",
    )
    adfs = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Active Directory Federation Services",
    )

    class Meta:
        model = Integration
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class CloudServiceForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['saas_sol'].label = False
        self.fields['iaas_hosted'].label = False
        self.fields['on_prem'].label = False
        self.helper.layout = Layout(
            InlineRadios('saas_sol'),
            InlineRadios('iaas_hosted'),
            InlineRadios('on_prem'),
        )

    saas_sol = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Is this a SaaS solution?",
    )
    iaas_hosted = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Is it hosted in IaaS owned by the Company?",
    )
    on_prem = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Is the solution built on premises in the Company's datacenter?",
    )

    class Meta:
        model = CloudService
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class SecureDesignForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1'].label = False
        self.fields['q2'].label = False
        self.fields['q3'].label = False
        self.fields['q4'].label = False
        self.fields['q5'].label = False
        self.fields['q6'].label = False
        self.helper.layout = Layout(
            InlineRadios('q1'),
            InlineRadios('q2'),
            InlineRadios('q3'),
            InlineRadios('q4'),
            InlineRadios('q5'),
            InlineRadios('q6'),
        )

    q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 1",
    )
    q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 2",
    )
    q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 3",
    )
    q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 4",
    )
    q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 5",
    )
    q6 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Design Question 6",
    )

    class Meta:
        model = SecureDesign
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class EncryptionForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['p1q1'].label = False
        self.fields['p1q2'].label = False
        self.fields['p1q3'].label = False
        self.fields['p1q4'].label = False
        self.fields['p1q5'].label = False
        self.fields['p1q6'].label = False
        self.fields['p1q7'].label = False
        self.fields['p1q8'].label = False
        self.fields['p1q9'].label = False
        self.fields['p2q1'].label = False
        self.fields['p2q2'].label = False
        self.fields['p2q3'].label = False
        self.fields['p2q4'].label = False
        self.fields['p2q5'].label = False
        self.fields['p2q6'].label = False
        self.fields['p2q7'].label = False
        self.helper.layout = Layout(
            InlineRadios('p1q1'),
            InlineRadios('p1q2'),
            InlineRadios('p1q3'),
            InlineRadios('p1q4'),
            InlineRadios('p1q5'),
            InlineRadios('p1q6'),
            InlineRadios('p1q7'),
            InlineRadios('p1q8'),
            InlineRadios('p1q9'),
            InlineRadios('p2q1'),
            InlineRadios('p2q2'),
            InlineRadios('p2q3'),
            InlineRadios('p2q4'),
            InlineRadios('p2q5'),
            InlineRadios('p2q6'),
            InlineRadios('p2q7'),
        )

    p1q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 1",
    )
    p1q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 2",
    )
    p1q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 3",
    )
    p1q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 4",
    )
    p1q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 5",
    )
    p1q6 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 6",
    )
    p1q7 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 7",
    )
    p1q8 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 8",
    )
    p1q9 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 1 - Question 9",
    )
    p2q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 1",
    )
    p2q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 2",
    )
    p2q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 3",
    )
    p2q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 4",
    )
    p2q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 5",
    )
    p2q6 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 6",
    )
    p2q7 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Encryption Part 2 - Question 7",
    )

    class Meta:
        model = Encryption
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class QAEnvironmentForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1'].label = False
        self.fields['q2'].label = False
        self.fields['q3'].label = False
        self.fields['q4'].label = False
        self.fields['q5'].label = False
        self.helper.layout = Layout(
            InlineRadios('q1'),
            InlineRadios('q2'),
            InlineRadios('q3'),
            InlineRadios('q4'),
            InlineRadios('q5'),
        )

    q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Quality Assurance Environment Question 1",
    )
    q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Quality Assurance Environment Question 2",
    )
    q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Quality Assurance Environment Question 3",
    )
    q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Quality Assurance Environment Question 4",
    )
    q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Quality Assurance Environment Question 5",
    )

    class Meta:
        model = QAEnvironment
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class DatabaseServersForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1'].label = False
        self.fields['q2'].label = False
        self.fields['q3'].label = False
        self.fields['q4'].label = False
        self.fields['q5'].label = False
        self.fields['q6'].label = False
        self.helper.layout = Layout(
            InlineRadios('q1'),
            InlineRadios('q2'),
            InlineRadios('q3'),
            InlineRadios('q4'),
            InlineRadios('q5'),
            InlineRadios('q6'),
        )

    q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 1",
    )
    q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 2",
    )
    q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 3",
    )
    q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 4",
    )
    q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 5",
    )
    q6 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Database Servers Question 6",
    )

    class Meta:
        model = DatabaseServers
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class SecureCommsForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1'].label = False
        self.fields['q2'].label = False
        self.fields['q3'].label = False
        self.fields['q4'].label = False
        self.fields['q5'].label = False
        self.fields['q6'].label = False
        self.fields['q7'].label = False
        self.fields['q8'].label = False
        self.helper.layout = Layout(
            InlineRadios('q1'),
            InlineRadios('q2'),
            InlineRadios('q3'),
            InlineRadios('q4'),
            InlineRadios('q5'),
            InlineRadios('q6'),
            InlineRadios('q7'),
            InlineRadios('q8'),
        )

    q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 1",
    )
    q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 2",
    )
    q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 3",
    )
    q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 4",
    )
    q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 5",
    )
    q6 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 6",
    )
    q7 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 7",
    )
    q8 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Secure Communications Question 8",
    )

    class Meta:
        model = SecureComms
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }


class SWIntegrityForm(ModelForm):

    BOOL_CHOICES = [("Yes", "Yes"), ("No", "No")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['q1'].label = False
        self.fields['q2'].label = False
        self.fields['q3'].label = False
        self.fields['q4'].label = False
        self.fields['q5'].label = False
        self.helper.layout = Layout(
            InlineRadios('q1'),
            InlineRadios('q2'),
            InlineRadios('q3'),
            InlineRadios('q4'),
            InlineRadios('q5'),
        )

    q1 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Software Integrity Question 1",
    )
    q2 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Software Integrity Question 2",
    )
    q3 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Software Integrity Question 3",
    )
    q4 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Software Integrity Question 4",
    )
    q5 = forms.ChoiceField(
        choices=BOOL_CHOICES,
        widget=RadioSelectButtonGroup(),
        label="Software Integrity Question 5",
    )

    class Meta:
        model = SWIntegrity
        fields = "__all__"
        exclude = ["score", "max_score", "eval_score"]
        widgets = {
            "comment": forms.Textarea(attrs={'class':'form-control','placeholder':'Add Comment'}),
            "vend_has_perm": forms.CheckboxInput(),
        }
