# Generated by Django 2.1.5 on 2019-05-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verhuur', '0005_auto_20190427_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='lokaal',
            name='contract',
            field=models.FileField(default=1, upload_to='contract'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tent',
            name='contract',
            field=models.FileField(default=1, upload_to='contract'),
            preserve_default=False,
        ),
    ]