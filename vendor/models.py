from django.db import models
from accounts.models import Account
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.  

class Vendor(models.Model):

    CATEGORY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Under Negotiation', 'Under Negotiation'),
    )

    name = models.CharField(verbose_name="Vendor Name", max_length=150, null=True)
    website = models.CharField(verbose_name="Vendor Website", max_length=200)
    address = models.CharField(verbose_name="Vendor Address", max_length=200)
    exstContract = models.CharField(verbose_name="Master Agreement", max_length=25, null=True, choices=CATEGORY)
    slug = models.SlugField(verbose_name="Vendor Slug", max_length=175, blank=True)

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

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name).title()

    if new_slug is not None:
        slug = new_slug
    qs = Vendor.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Vendor)