# Generated by Django 3.1.7 on 2021-04-26 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_userdepartment_title'),
        ('riskassessment', '0020_auto_20210421_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskassessment',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='department.department', verbose_name='Department'),
        ),
    ]
