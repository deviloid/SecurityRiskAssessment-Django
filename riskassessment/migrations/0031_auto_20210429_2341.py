# Generated by Django 3.1.7 on 2021-04-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskassessment', '0030_auto_20210429_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskassessment',
            name='approve_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Date Approved'),
        ),
    ]
