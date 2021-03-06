# Generated by Django 3.1.7 on 2021-04-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210418_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='department',
        ),
        migrations.RemoveField(
            model_name='product',
            name='dept_mpc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='risk_analyst',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vend_mpc',
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Product Link'),
        ),
        migrations.AddField(
            model_name='product',
            name='tech_phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Technical Support Phone Number'),
        ),
    ]
