from django.db import models
from django.db.models.deletion import DO_NOTHING
from accounts.models import Account
from department.models import Department, UserDepartment
from vendor.models import Vendor, UserVendor

# Create your models here.
class Project(models.Model):
    name = models.CharField("Project Name", max_length=50, null=True)
    purpose = models.TextField("Project Purpose", max_length=500, null=True)
    department = models.ForeignKey(Department, on_delete=DO_NOTHING)
    vendor =  models.ForeignKey(Vendor, on_delete=DO_NOTHING)
    risk_analyst = models.ForeignKey(Account, verbose_name="Risk Analyst", on_delete=DO_NOTHING)
    dept_mpc = models.ForeignKey(UserDepartment, verbose_name='Main Project Contact Department', on_delete=DO_NOTHING)
    vend_mpc = models.ForeignKey(UserVendor, verbose_name='Main Project Contact Vendor', on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return self.name