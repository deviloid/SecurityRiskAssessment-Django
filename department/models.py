from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.query import QuerySet
from accounts.models import Account
from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
    name = models.CharField("Department Name", max_length=200)
    location = models.CharField("Department Location", max_length=200, null=True, blank=True)
    slug = models.SlugField(verbose_name="Slug", max_length=250, blank=True)

    def __str__(self) -> str:
        return self.name



class UserTypeDepartment(models.Model):
    
    CATEGORY = (
        ('Main Project Contact', 'Main Project Contact'),
        ('Technical Administrator', 'Technical Administrator'),
        ('End-User Requestor', 'End-User Requestor'),
    )    

    name = models.CharField(verbose_name="User Type", max_length=35, null=True, choices=CATEGORY)

    def __str__(self) -> str:
        return self.name



class UserDepartment(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Designation Title", max_length=200, null=True, blank=True)
    # fname = models.CharField("First Name", max_length=50, null=True)
    # lname = models.CharField("Last Name", max_length=50, null=True)
    # phone = models.CharField(max_length=10, null=True)
    # email = models.CharField(max_length=100, null=True)
    department =  models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    userType = models.ForeignKey('UserTypeDepartment', on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=10, null=False)


    def __str__(self) -> str:
        return self.user.fname + " " + self.user.lname