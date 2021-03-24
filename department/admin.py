from django.contrib import admin
from department.models import UserDepartment

from .models import *

# Register your models here.


admin.site.register(Department)
admin.site.register(UserDepartment)
admin.site.register(UserTypeDepartment)

