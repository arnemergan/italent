# Generated by Django 2.1.5 on 2019-04-10 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inschrijven', '0003_auto_20190410_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lid',
            old_name='groepid',
            new_name='groep',
        ),
        migrations.RemoveField(
            model_name='leiding',
            name='groepid',
        ),
        migrations.AddField(
            model_name='leiding',
            name='groep',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='inschrijven.Groep'),
            preserve_default=False,
        ),
    ]
