# Generated by Django 2.1.5 on 2019-04-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0012_leiding_lid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groep',
            name='naam',
            field=models.CharField(choices=[('Leeuwkes', 'Leeuwkes'), ('Jong Knapen', 'Jong Knapen'), ('Knapen', 'Knapen'), ('Jong Hernieuwers', 'Jong Hernieuwers'), ('Hernieuwers', 'Hernieuwers'), ('+16', '+16'), ('Leiding', 'Leiding')], max_length=20),
        ),
    ]