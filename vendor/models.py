from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from accounts.models import Account

# Create your models here.  

class Vendor(models.Model):

    CATEGORY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Under Negotiation', 'Under Negotiation'),
    )

    name = models.CharField("Vendor Name", max_length=150, null=True)
    website = models.CharField("Vendor Website", max_length=200, null=True)
    exstContract = models.CharField("Do you have an existing signed contract with the Company?", max_length=25, null=True, choices=CATEGORY)

    def __str__(self) -> str:
        return self.name
    


class UserTypeVendor(models.Model):

    CATEGORY = (
        ('Vendor Contact', 'Vendor Contact'),
        ('Vendor Technical Contact', 'Vendor Technical Contact'),
        ('Technical Administrator', 'Technical Administrator'),
    )

    name = models.CharField("User Type", max_length=35, null=True, choices=CATEGORY)

    def __str__(self) -> str:
        return self.name



class UserVendor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # fname = models.CharField("First Name", max_length=50, null=True)
    # lname = models.CharField("Last Name", max_length=50, null=True)
    # phone = models.CharField(max_length=10, null=True)
    # email = models.CharField(max_length=100, null=True)
    vendor =  models.ForeignKey('Vendor', on_delete=models.CASCADE, null=True, blank=True)
    userType = models.ForeignKey('UserTypeVendor', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        # if self.userType == None:
        #     return self.user.fname + " " + self.user.lname
        # else:
        #     return self.user.fname + " " + self.user.lname + " - " + self.userType
        return self.user.fname + " " + self.user.lname