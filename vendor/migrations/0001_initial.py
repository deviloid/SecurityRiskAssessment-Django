# Generated by Django 3.1.7 on 2021-03-17 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTypeVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Vendor Contact', 'Vendor Contact'), ('Vendor Technical Contact', 'Vendor Technical Contact'), ('Technical Administrator', 'Technical Administrator')], max_length=35, null=True, verbose_name='User Type')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Vendor Name')),
                ('website', models.CharField(max_length=200, null=True, verbose_name='Vendor Website')),
                ('exstContract', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Under Negotiation', 'Under Negotiation')], max_length=25, null=True, verbose_name='Do you have an existing signed contract with the Company?')),
            ],
        ),
        migrations.CreateModel(
            name='UserVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.usertypevendor')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
