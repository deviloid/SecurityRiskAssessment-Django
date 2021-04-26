# Generated by Django 3.1.7 on 2021-04-19 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('riskassessment', '0002_auto_20210418_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.CharField(blank=True, default=None, max_length=6, null=True, verbose_name='Assessment Score')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Product')),
            ],
        ),
    ]