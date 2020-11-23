# Generated by Django 2.2.17 on 2020-11-23 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0077_auto_20201104_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundprocess',
            name='process_class_kwargs',
            field=models.CharField(blank=True, default='{}', help_text='arguments in json format will be passed as kwargs while the\n                                            init of the process instance, example:\n                                            {"keywordA":"value1", "keywordB":7}', max_length=400),
        ),
        migrations.AlterField(
            model_name='complexeventitem',
            name='variable_limit_high',
            field=models.ForeignKey(blank=True, default=None, help_text='you can choose either an\n                                            fixed limit or an variable limit that is dependent on the current value of\n                                            an variable, if you choose a value other than  none for variable limit the\n                                            fixed limit would be ignored', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variable_limit_high', to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='complexeventitem',
            name='variable_limit_low',
            field=models.ForeignKey(blank=True, default=None, help_text='you can choose either an\n                                            fixed limit or an variable limit that is dependent on the current value of\n                                            an variable, if you choose a value other than  none for variable limit the\n                                            fixed limit would be ignored', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variable_limit_low', to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='devicereadtask',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='devicereadtask',
            name='variable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='devicereadtask',
            name='variable_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.VariableProperty'),
        ),
        migrations.AlterField(
            model_name='devicewritetask',
            name='variable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='devicewritetask',
            name='variable_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.VariableProperty'),
        ),
        migrations.AlterField(
            model_name='event',
            name='variable_limit',
            field=models.ForeignKey(blank=True, default=None, help_text='you can choose either an fixed limit or an variable limit that is\n                                        dependent on the current value of an variable, if you choose a value other than\n                                        none for variable limit the fixed limit would be ignored', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variable_limit', to='pyscada.Variable'),
        ),
    ]
