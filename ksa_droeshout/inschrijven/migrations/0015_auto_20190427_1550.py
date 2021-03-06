# Generated by Django 2.1.5 on 2019-04-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0014_auto_20190423_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groep',
            name='beschrijving',
            field=models.TextField(max_length=750),
        ),
        migrations.AlterField(
            model_name='groep',
            name='groepfoto',
            field=models.ImageField(upload_to='images/groep'),
        ),
        migrations.AlterField(
            model_name='inschrijving',
            name='brief',
            field=models.FileField(upload_to='brieven'),
        ),
        migrations.AlterField(
            model_name='leiding',
            name='foto',
            field=models.ImageField(upload_to='images/leiding'),
        ),
    ]
