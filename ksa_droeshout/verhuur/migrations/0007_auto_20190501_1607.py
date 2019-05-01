# Generated by Django 2.1.5 on 2019-05-01 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verhuur', '0006_auto_20190501_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokaal',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inschrijven.Leiding'),
        ),
        migrations.AlterField(
            model_name='materiaal',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inschrijven.Leiding'),
        ),
        migrations.AlterField(
            model_name='tent',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inschrijven.Leiding'),
        ),
    ]
