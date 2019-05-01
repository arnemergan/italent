# Generated by Django 2.1.5 on 2019-04-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0016_auto_20190428_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_geg',
            name='tel',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact_geg',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
