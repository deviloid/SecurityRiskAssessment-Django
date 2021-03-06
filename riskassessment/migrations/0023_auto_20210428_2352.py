# Generated by Django 3.1.7 on 2021-04-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskassessment', '0022_auto_20210427_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabiltycriticality',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='cloudservice',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='compliance',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='databaseservers',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='datamanagement',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='encryption',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='integration',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='qaenvironment',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='secmatevidence',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='securecomms',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='securedesign',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
        migrations.AlterField(
            model_name='swintegrity',
            name='eval_score',
            field=models.IntegerField(default=-1, verbose_name='Evaluated Score'),
        ),
    ]
