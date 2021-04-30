from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import pre_save
from django.utils.text import slugify

from accounts.models import Account
from department.models import Department, UserDepartment
from vendor.models import Vendor, UserVendor

    #TODO Move to Risk Assessment
    #TODO Make Changes to Form
    #TODO Make Changes to Website
    #TODO Add technical support contact
    #TODO Add software link

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="Product Name", max_length=50, null=True)
    purpose = models.TextField(verbose_name="Product Purpose", max_length=500, null=True)
    tech_phone = models.CharField(verbose_name="Technical Support Phone Number", max_length=10, blank=True, null=True)
    link = models.CharField(verbose_name="Product Link", max_length=200, blank=True, null=True)
    vendor =  models.ForeignKey(Vendor, on_delete=DO_NOTHING)
    # department = models.ForeignKey(Department, on_delete=DO_NOTHING)
    # risk_analyst = models.ForeignKey(Account, verbose_name="Risk Analyst", on_delete=DO_NOTHING)
    # dept_mpc = models.ForeignKey(UserDepartment, verbose_name='Main Project Contact Department', on_delete=DO_NOTHING)
    # vend_mpc = models.ForeignKey(UserVendor, verbose_name='Main Project Contact Vendor', on_delete=DO_NOTHING)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name).title()
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Product)