# Generated by Django 4.0 on 2021-12-18 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addAlgo', '0003_addalgorithm_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addalgorithm',
            name='output',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Output'),
        ),
    ]