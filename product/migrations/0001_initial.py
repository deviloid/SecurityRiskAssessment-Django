# Generated by Django 3.1.7 on 2021-04-13 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0004_auto_20210319_0313'),
        ('vendor', '0005_auto_20210322_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Product Name')),
                ('purpose', models.TextField(max_length=500, null=True, verbose_name='Product Purpose')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='department.department')),
                ('dept_mpc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='department.userdepartment', verbose_name='Main Project Contact Department')),
                ('risk_analyst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Risk Analyst')),
                ('vend_mpc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendor.uservendor', verbose_name='Main Project Contact Vendor')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendor.vendor')),
            ],
        ),
    ]