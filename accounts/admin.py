from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'fname', 'lname', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('fname', 'lname', 'email')
    readonly_fields = ('id', 'date_joined', 'last_login')
    

    filter_horizontal = ()
    list_filter = ()
    
    fieldsets = (
        ('Details',{'fields': ('fname', 'lname', 'email', 'password')}),
        ('Permissions',{'fields': ('is_admin', 'is_staff', 'is_userdepartment', 'is_uservendor')}),
        ('Logs',{'fields': ('has_setpsd', 'date_joined', 'last_login')}),
    )

    add_fieldsets = (
        ('Details',{'fields': ('fname', 'lname', 'email', 'password1', 'password2')}),
    )

    # inlines = (UserDepartmentInline, UserVendorInline)

admin.site.register(Account, AccountAdmin)

# from department.models import UserDepartment
# from vendor.models import UserVendor

# Register your models here.

# class UserDepartmentInline(admin.StackedInline):
#     model = UserDepartment
#     can_delete = False
#     verbose_name_plural = 'Users - Department'
#     verbose_name = 'Users - Department'

# class UserVendorInline(admin.StackedInline):
#     model = UserVendor
#     can_delete = False
#     verbose_name_plural = 'Users - Vendor'
#     verbose_name = 'Users - Vendor'