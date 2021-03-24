from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField("Project Name", max_length=50, null=True)
    purpose = models.TextField("Project Purpose", max_length=500, null=True)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    vendor =  models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name + " - " + self.department.name + " - " + self.vendor.name