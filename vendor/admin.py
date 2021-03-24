from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Vendor)
admin.site.register(UserVendor)
admin.site.register(UserTypeVendor)