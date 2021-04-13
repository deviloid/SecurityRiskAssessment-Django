from django.db import models
from django.db.models.deletion import DO_NOTHING
from project.models import Project
from department.models import Department

# Create your models here.
class DeptInfo(models.Model):

    class Meta:
        verbose_name = 'Department Information'
        verbose_name_plural = 'Department Information'

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
    )
    ta_name = models.CharField(verbose_name="Name", max_length=100)
    ta_email = models.EmailField(verbose_name="Email", max_length=100)
    ta_phone = models.CharField(verbose_name="Phone", max_length=10)
    eur_name = models.CharField(verbose_name="Name", max_length=100)
    eur_email = models.EmailField(verbose_name="Email", max_length=100)
    eur_phone = models.CharField(verbose_name="Phone", max_length=10)
    ds_name = models.CharField(verbose_name="Name", max_length=100)
    ds_email = models.EmailField(verbose_name="Email", max_length=100)
    ds_phone = models.CharField(verbose_name="Phone", max_length=10)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class VendInfo(models.Model):

    class Meta:
        verbose_name = 'Vendor Information'
        verbose_name_plural = 'Vendor Information'

    CHOICES = (("Yes", "Yes"), ("No", "No"), ("Under Negotiation", "Under Negotiation"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
    )
    tc_name = models.CharField(verbose_name="Name", max_length=100)
    tc_email = models.EmailField(verbose_name="Email", max_length=100)
    tc_phone = models.CharField(verbose_name="Phone", max_length=10)
    exst_contract = models.CharField(max_length=18, choices=CHOICES)
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class DataManagement(models.Model):

    class Meta:
        verbose_name = 'Data Management'
        verbose_name_plural = 'Data Management'

    RD_CHOICES = (
        ("FERPA", "FERPA"),
        ("HIPAA", "HIPAA"),
        ("GDPR", "GDPR"),
        ("ITAR", "ITAR"),
        ("PCI", "PCI"),
        ("PII", "PII"),
    )

    DC_CHOICES = (
        ("Highly Sensitive", "Highly Sensitive"),
        ("Sensitive", "Sensitive"),
        ("Internal", "Internal"),
        ("Public", "Public"),
    )

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    INT_CHOICES = (
        ("500", "500"),
        ("1000", "1000"),
        ("2000", "2000"),
        ("3000", "3000"),
        ("4000", "4000"),
        ("5000", "5000"),
        ("6000", "6000"),
        ("7000", "7000"),
    )

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
    )
    reg_data = models.CharField(verbose_name="Regulated Data", max_length=5)
    data_classi = models.CharField(verbose_name="Data Classification", max_length=16)
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
        verbose_name="Is any data received (directly or indirectly by ASU) from individuals outside of the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    data_accss_outside = models.CharField(
        verbose_name="Are data or Systems accessible outside the US?",
        max_length=3,
        choices=BOOL_CHOICES,
    )
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class AvailabiltyCriticality(models.Model):

    class Meta:
        verbose_name = 'Availabilty and Criticality'
        verbose_name_plural = 'Availabilty and Criticality'

    A_CHOICES = (("Tier 1", "Tier 1"), ("Tier 2", "Tier 2"), ("Tier 3", "Tier 3"))
    C_CHOICES = (("High", "High"), ("Medium", "Medium"), ("Low", "Low"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
    )
    a_rating = models.CharField(
        verbose_name="Availability Rating", max_length=6, choices=A_CHOICES
    )
    c_rating = models.CharField(
        verbose_name="Criticality Rating", max_length=6, choices=C_CHOICES
    )
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class Compliance(models.Model):

    class Meta:
        verbose_name = 'Compliance'
        verbose_name_plural = 'Compliance'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class SecMatEvidence(models.Model):

    class Meta:
        verbose_name = 'Security Maturity Evidence'
        verbose_name_plural = 'Security Maturity Evidence'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class Integration(models.Model):

    class Meta:
        verbose_name = 'Integration'
        verbose_name_plural = 'Integration'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class CloudService(models.Model):

    class Meta:
        verbose_name = 'Cloud Service Model'
        verbose_name_plural = 'Cloud Service Model'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class SecureDesign(models.Model):

    class Meta:
        verbose_name = 'Secure Design'
        verbose_name_plural = 'Secure Design'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class Encryption(models.Model):

    class Meta:
        verbose_name = 'Encryption'
        verbose_name_plural = 'Encryption'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class QAEnvironment(models.Model):

    class Meta:
        verbose_name = 'Quality Assurance Environment'
        verbose_name_plural = 'Quality Assurance Environment'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class DatabaseServers(models.Model):

    class Meta:
        verbose_name = 'Database Servers'
        verbose_name_plural = 'Database Servers'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class SecureComms(models.Model):

    class Meta:
        verbose_name = 'Secure Communications'
        verbose_name_plural = 'Secure Communications'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)


class SWIntegrity(models.Model):

    class Meta:
        verbose_name = 'Software Integrity'
        verbose_name_plural = 'Software Integrity'

    BOOL_CHOICES = (("Yes", "Yes"), ("No", "No"))

    project = models.OneToOneField(
        Project, verbose_name="Project", on_delete=DO_NOTHING
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
    vend_has_perm = models.BooleanField(verbose_name="Vendor can edit?", default=False)
