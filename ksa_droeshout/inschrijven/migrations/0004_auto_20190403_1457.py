# Generated by Django 2.1.5 on 2019-04-03 12:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0003_inschrijving_actief'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lid',
            name='id',
        ),
        migrations.AddField(
            model_name='lid',
            name='actief',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lid',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
