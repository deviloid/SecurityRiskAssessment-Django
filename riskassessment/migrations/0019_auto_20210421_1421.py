# Generated by Django 3.1.7 on 2021-04-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskassessment', '0018_auto_20210421_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabiltycriticality',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='cloudservice',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='compliance',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='databaseservers',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='datamanagement',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='deptinfo',
            name='eval_max_score',
            field=models.IntegerField(default=0, verbose_name='Maxed Score'),
        ),
        migrations.AddField(
            model_name='encryption',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='integration',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='qaenvironment',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='secmatevidence',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='securecomms',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='securedesign',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='swintegrity',
            name='eval_score',
            field=models.IntegerField(default=0, verbose_name='Evaluated Score'),
        ),
        migrations.AddField(
            model_name='vendinfo',
            name='eval_max_score',
            field=models.IntegerField(default=0, verbose_name='Maxed Score'),
        ),
        migrations.AlterField(
            model_name='availabiltycriticality',
            name='max_score',
            field=models.IntegerField(default=10, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='cloudservice',
            name='max_score',
            field=models.IntegerField(default=3, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='compliance',
            name='max_score',
            field=models.IntegerField(default=9, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='databaseservers',
            name='max_score',
            field=models.IntegerField(default=13, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='datamanagement',
            name='max_score',
            field=models.IntegerField(default=15, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='deptinfo',
            name='max_score',
            field=models.IntegerField(default=0, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='encryption',
            name='max_score',
            field=models.IntegerField(default=41, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='integration',
            name='max_score',
            field=models.IntegerField(default=9, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='qaenvironment',
            name='max_score',
            field=models.IntegerField(default=12, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='secmatevidence',
            name='max_score',
            field=models.IntegerField(default=12, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='securecomms',
            name='max_score',
            field=models.IntegerField(default=20, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='securedesign',
            name='max_score',
            field=models.IntegerField(default=19, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='swintegrity',
            name='max_score',
            field=models.IntegerField(default=12, verbose_name='Max Score'),
        ),
        migrations.AlterField(
            model_name='vendinfo',
            name='max_score',
            field=models.IntegerField(default=0, verbose_name='Max Score'),
        ),
    ]
