# Generated by Django 2.1.5 on 2019-04-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verhuur', '0003_lokaal_waarborg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tent',
            old_name='prijsperstuk',
            new_name='prijsnwinst',
        ),
        migrations.AddField(
            model_name='tent',
            name='prijswinst',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tent',
            name='waarborg',
            field=models.DecimalField(decimal_places=2, default=21, max_digits=5),
            preserve_default=False,
        ),
    ]
