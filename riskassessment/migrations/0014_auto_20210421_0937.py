# Generated by Django 3.1.7 on 2021-04-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskassessment', '0013_auto_20210421_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deptinfo',
            name='comment',
        ),
        migrations.AlterField(
            model_name='availabiltycriticality',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='cloudservice',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='compliance',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='databaseservers',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='datamanagement',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='encryption',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='integration',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='qaenvironment',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='secmatevidence',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='securecomms',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='securedesign',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='swintegrity',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment'),
        ),
    ]
