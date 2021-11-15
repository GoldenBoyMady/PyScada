# Generated by Django 2.2.24 on 2021-11-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0083_auto_20211115_0812'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VariableCalculatedFields',
            new_name='CalculatedVariableSelector',
        ),
        migrations.RenameModel(
            old_name='PeriodField',
            new_name='PeriodicField',
        ),
        migrations.AddField(
            model_name='calculatedvariable',
            name='last_check',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
