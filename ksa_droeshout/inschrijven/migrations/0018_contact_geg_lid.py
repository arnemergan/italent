# Generated by Django 2.1.5 on 2019-04-30 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0017_auto_20190430_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_geg',
            name='lid',
            field=models.ForeignKey(default='44ee6267-1eca-4cdc-be59-b9d6558d555b', on_delete=django.db.models.deletion.CASCADE, to='inschrijven.Lid'),
            preserve_default=False,
        ),
    ]
