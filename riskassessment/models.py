from django.http import request
from accounts.models import Account
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import pre_save

from datetime import date

from product.models import Product
from department.models import Department, UserDepartment
from vendor.models import UserVendor

# Create your models here.
class RiskAssessment(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=DO_NOTHING)
    ra_number = models.CharField(verbose_name="RA Number", max_length=8, blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="Department", null=True, blank=True, on_delete=DO_NOTHING)
    date = models.DateField(verbose_name='Date Added', auto_now_add=True)
    steps_complete = models.IntegerField(verbose_name="Steps Completed", default=0)
    total_score = models.CharField(verbose_name='Assessment Score', max_length=6, default=None, blank=True, null=True)
    evaluated = models.BooleanField(verbose_name="Evaluated?", default=False)
    approved = models.BooleanField(verbose_name="Approved?", default=False)
    ra = models.ForeignKey(Account, verbose_name="Risk Analyst", on_delete=DO_NOTHING)

    def __str__(self) -> str:
        if self.total_score != None:
            return str(self.product) + " - " + str(self.total_score)
        else:
            return str(self.product) + " - " + str(self.id) + " - " + "No Score" + " - " + str(self.date)


            # ra.ra_number = str(int(date.today().year)*1000 + ra.id)


def create_ra_number(instance, new_slug=None):
    count = RiskAssessment.objects.filter(date__year=date.today().year).count() + 1
    ra_number = str(int(date.today().year)*10000 + count)

    return ra_number


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.ra_number:
        instance.ra_number = create_ra_number(instance)

pre_save.connect(pre_save_post_receiver, sender=RiskAssessment)




class DeptInfo(models.Model):

    class Meta:
        verbose_name = 'Department Information'
        verbose_name_plural = 'Department Information'

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step1'
    )
    mpc = models.ForeignKey(UserDepartment, verbose_name='Main Project Contact', on_delete=DO_NOTHING, blank=True, null=True)
    ta_dept = models.ForeignKey(Department, verbose_name="Department", related_name="ta_dept", on_delete=DO_NOTHING, blank=True)
    ta_name = models.CharField(verbose_name="Name", max_length=100)
    ta_email = models.EmailField(verbose_name="Email", max_length=100)
    ta_phone = models.CharField(verbose_name="Phone", max_length=10)
    eur_dept = models.ForeignKey(Department, verbose_name="Department", related_name="eur_dept", on_delete=DO_NOTHING, blank=True)
    eur_name = models.CharField(verbose_name="Name", max_length=100)
    eur_email = models.EmailField(verbose_name="Email", max_length=100)
    eur_phone = models.CharField(verbose_name="Phone", max_length=10)
    ds_dept = models.ForeignKey(Department, verbose_name="Department", related_name="ds_dept", on_delete=DO_NOTHING, blank=True)
    ds_name = models.CharField(verbose_name="Name", max_length=100)
    ds_email = models.EmailField(verbose_name="Email", max_length=100)
    ds_phone = models.CharField(verbose_name="Phone", max_length=10)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=0)
    eval_score = models.IntegerField(verbose_name="Maxed Score", default=0)


    def __str__(self) -> str:
        return str(self.riskassessment)


class VendInfo(models.Model):

    class Meta:
        verbose_name = 'Vendor Information'
        verbose_name_plural = 'Vendor Information'

    CHOICES = (("Yes", "Yes"), ("No", "No"), ("Under Negotiation", "Under Negotiation"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step2'
    )
    # mpc = models.ForeignKey(UserVendor, verbose_name='Main Project Contact', on_delete=DO_NOTHING, blank=True, null=True)
    mpc_name = models.CharField(verbose_name="Vendor Primary Contact Name", max_length=100, blank=True)
    mpc_email = models.EmailField(verbose_name="Vendor Primary Contact Email", max_length=100, blank=True)
    mpc_phone = models.CharField(verbose_name="Vendor Primary Contact Phone", max_length=10, blank=True)
    tc_name = models.CharField(verbose_name="Technical Contact Name", max_length=100)
    tc_email = models.EmailField(verbose_name="Technical Contact Email", max_length=100)
    tc_phone = models.CharField(verbose_name="Technical Contact Phone", max_length=10)
    exst_contract = models.CharField(verbose_name="Master Agreement?", max_length=18, choices=CHOICES)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=0)
    eval_score = models.IntegerField(verbose_name="Maxed Score", default=0)


    def __str__(self) -> str:
        return str(self.riskassessment)

class RegulatedData(models.Model):
    class Meta:
        verbose_name = "Regulated Data"
        verbose_name_plural = "Regulated Data"
    
    name = models.CharField(verbose_name="Data Type", max_length=6)

    def __str__(self) -> str:
        return self.name


class DataClassification(models.Model):
    class Meta:
        verbose_name = "Data Classification"
        verbose_name_plural = "Data Classification"
    
    name = models.CharField(verbose_name="Sensitivity", max_length=16)

    def __str__(self) -> str:
        return self.name


class DataManagement(models.Model):

    class Meta:
        verbose_name = 'Data Management'
        verbose_name_plural = 'Data Management'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    INT_CHOICES = (
        (500, 500),
        (1000, 1000),
        (2000, 2000),
        (3000, 3000),
        (4000, 4000),
        (5000, 5000),
        (6000, 6000),
        (7000, 7000),
    )

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step3'
    )
    reg_data = models.ManyToManyField(RegulatedData, verbose_name="Regulated Data")
    data_classi = models.ManyToManyField(DataClassification, verbose_name="Data Classification")
    recs_in_data = models.IntegerField(
        verbose_name="Number of Records in Data", choices=INT_CHOICES
    )
    recs_purged = models.CharField(
        verbose_name="Are records purged from Data?", max_length=3, choices=BOOL_CHOICES
    )
    est_add_recs = models.IntegerField(
        verbose_name="Estimated yearly additional records", choices=INT_CHOICES
    )
    data_process_outside = models.CharField(
        verbose_name="Is data processing performed outside the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    data_stored_outside = models.CharField(
        verbose_name="Is data stored outside the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    data_rcvd_outside = models.CharField(
        verbose_name="Is any data received (directly or indirectly by Company) from individuals outside of the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    data_accss_outside = models.CharField(
        verbose_name="Are data or Systems accessible outside the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=15)


class AvailabiltyCriticality(models.Model):

    class Meta:
        verbose_name = 'Availabilty and Criticality'
        verbose_name_plural = 'Availabilty and Criticality'

    A_CHOICES = (("Tier 1", "Tier 1"), ("Tier 2", "Tier 2"), ("Tier 3", "Tier 3"))
    C_CHOICES = (("High", "High"), ("Medium", "Medium"), ("Low", "Low"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step4'
    )
    a_rating = models.CharField(
        verbose_name="Availability Rating", max_length=6, choices=A_CHOICES
    )
    c_rating = models.CharField(
        verbose_name="Criticality Rating", max_length=6, choices=C_CHOICES
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=10)


class Compliance(models.Model):

    class Meta:
        verbose_name = 'Compliance'
        verbose_name_plural = 'Compliance'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step5'
    )
    sso = models.CharField(
        verbose_name="Single Sign-on Systems?", max_length=3, choices=BOOL_CHOICES
    )
    audit_req_std_comp = models.CharField(
        verbose_name="Company System Audit Requirements Standard Compliant?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    auto_patch = models.CharField(
        verbose_name="Vendor Provides automated patching?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=9)


class SecMatEvidence(models.Model):

    class Meta:
        verbose_name = 'Security Maturity Evidence'
        verbose_name_plural = 'Security Maturity Evidence'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step6'
    )
    attst_o_comp = models.CharField(
        verbose_name="Attestation of Compliance", max_length=3, choices=BOOL_CHOICES
    )
    soc2_reports = models.CharField(
        verbose_name="Current system’s vendor 3rd party SOC2 Type 2 reports",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    ann_pen_scan_results = models.CharField(
        verbose_name="Annual penetration/vulnerability scanning results of all system components",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    ann_wa_vuln_scan = models.CharField(
        verbose_name="Annual web application vulnerability scan of all system web applications",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=12)


class Integration(models.Model):

    class Meta:
        verbose_name = 'Integration'
        verbose_name_plural = 'Integration'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step7'
    )
    sso = models.CharField(
        verbose_name="Single Sign-on", max_length=3, choices=BOOL_CHOICES
    )
    mfa = models.CharField(
        verbose_name="Multi-Factor Authentication", max_length=3, choices=BOOL_CHOICES
    )
    adfs = models.CharField(
        verbose_name="Active Directory Federation Services",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=9)


class CloudService(models.Model):

    class Meta:
        verbose_name = 'Cloud Service Model'
        verbose_name_plural = 'Cloud Service Model'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step8'
    )
    saas_sol = models.CharField(
        verbose_name="Is this a SaaS solution?", max_length=3, choices=BOOL_CHOICES
    )
    iaas_hosted = models.CharField(
        verbose_name="Is it hosted in IaaS owned by the Company?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    on_prem = models.CharField(
        verbose_name="Is the solution built on premises in the Company's datacenter?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=3)


class SecureDesign(models.Model):

    class Meta:
        verbose_name = 'Secure Design'
        verbose_name_plural = 'Secure Design'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step9'
    )
    q1 = models.CharField(
        verbose_name="Secure Design Question 1", max_length=3, choices=BOOL_CHOICES
    )
    q2 = models.CharField(
        verbose_name="Secure Design Question 2", max_length=3, choices=BOOL_CHOICES
    )
    q3 = models.CharField(
        verbose_name="Secure Design Question 3", max_length=3, choices=BOOL_CHOICES
    )
    q4 = models.CharField(
        verbose_name="Secure Design Question 4", max_length=3, choices=BOOL_CHOICES
    )
    q5 = models.CharField(
        verbose_name="Secure Design Question 5", max_length=3, choices=BOOL_CHOICES
    )
    q6 = models.CharField(
        verbose_name="Secure Design Question 6", max_length=3, choices=BOOL_CHOICES
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=19)


class Encryption(models.Model):

    class Meta:
        verbose_name = 'Encryption'
        verbose_name_plural = 'Encryption'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step10'
    )
    p1q1 = models.CharField(
        verbose_name="Encryption Part 1 - Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q2 = models.CharField(
        verbose_name="Encryption Part 1 - Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q3 = models.CharField(
        verbose_name="Encryption Part 1 - Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q4 = models.CharField(
        verbose_name="Encryption Part 1 - Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q5 = models.CharField(
        verbose_name="Encryption Part 1 - Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q6 = models.CharField(
        verbose_name="Encryption Part 1 - Question 6",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q7 = models.CharField(
        verbose_name="Encryption Part 1 - Question 7",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q8 = models.CharField(
        verbose_name="Encryption Part 1 - Question 8",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p1q9 = models.CharField(
        verbose_name="Encryption Part 1 - Question 9",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q1 = models.CharField(
        verbose_name="Encryption Part 2 - Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q2 = models.CharField(
        verbose_name="Encryption Part 2 - Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q3 = models.CharField(
        verbose_name="Encryption Part 2 - Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q4 = models.CharField(
        verbose_name="Encryption Part 2 - Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q5 = models.CharField(
        verbose_name="Encryption Part 2 - Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q6 = models.CharField(
        verbose_name="Encryption Part 2 - Question 6",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    p2q7 = models.CharField(
        verbose_name="Encryption Part 2 - Question 7",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=41)


class QAEnvironment(models.Model):

    class Meta:
        verbose_name = 'Quality Assurance Environment'
        verbose_name_plural = 'Quality Assurance Environment'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step11'
    )
    q1 = models.CharField(
        verbose_name="Quality Assurance Environment Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q2 = models.CharField(
        verbose_name="Quality Assurance Environment Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q3 = models.CharField(
        verbose_name="Quality Assurance Environment Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q4 = models.CharField(
        verbose_name="Quality Assurance Environment Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q5 = models.CharField(
        verbose_name="Quality Assurance Environment Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=12)


class DatabaseServers(models.Model):

    class Meta:
        verbose_name = 'Database Servers'
        verbose_name_plural = 'Database Servers'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step12'
    )
    q1 = models.CharField(
        verbose_name="Database Servers Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q2 = models.CharField(
        verbose_name="Database Servers Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q3 = models.CharField(
        verbose_name="Database Servers Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q4 = models.CharField(
        verbose_name="Database Servers Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q5 = models.CharField(
        verbose_name="Database Servers Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q6 = models.CharField(
        verbose_name="Database Servers Question 6",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=13)


class SecureComms(models.Model):

    class Meta:
        verbose_name = 'Secure Communications'
        verbose_name_plural = 'Secure Communications'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step13'
    )
    q1 = models.CharField(
        verbose_name="Secure Communications Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q2 = models.CharField(
        verbose_name="Secure Communications Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q3 = models.CharField(
        verbose_name="Secure Communications Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q4 = models.CharField(
        verbose_name="Secure Communications Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q5 = models.CharField(
        verbose_name="Secure Communications Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q6 = models.CharField(
        verbose_name="Secure Communications Question 6",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q7 = models.CharField(
        verbose_name="Secure Communications Question 7",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q8 = models.CharField(
        verbose_name="Secure Communications Question 8",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=20)


class SWIntegrity(models.Model):

    class Meta:
        verbose_name = 'Software Integrity'
        verbose_name_plural = 'Software Integrity'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    riskassessment = models.ForeignKey(
        RiskAssessment, verbose_name="Risk Assessment", on_delete=DO_NOTHING, related_name='ra_step14'
    )
    q1 = models.CharField(
        verbose_name="Software Integrity Question 1",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q2 = models.CharField(
        verbose_name="Software Integrity Question 2",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q3 = models.CharField(
        verbose_name="Software Integrity Question 3",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q4 = models.CharField(
        verbose_name="Software Integrity Question 4",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    q5 = models.CharField(
        verbose_name="Software Integrity Question 5",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    comment = models.TextField(verbose_name="Comment", max_length=1000, blank=True, null=True)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
    score = models.IntegerField(verbose_name="Section Score", default=0)
    eval_score = models.IntegerField(verbose_name="Evaluated Score", default=-1)
    max_score = models.IntegerField(verbose_name="Max Score", default=12)
